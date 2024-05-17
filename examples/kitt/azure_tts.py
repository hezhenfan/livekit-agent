import os
import re
import uuid

import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechSynthesisOutputFormat

speech_key, service_region = "e5a8143f92bc4da3a69fdeb1ddfe70dc", "eastus"


def gen_audio(text: str):
    # Creates an instance of a speech config with specified subscription key and service region.
    # speech_key = "undefined"
    # service_region = "undefined"

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = "zh-CN-XiaoxiaoMultilingualNeural"
    speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat.Audio16Khz128KBitRateMonoMp3)

    # use the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    # speechsdk.SpeechRecognitionResult(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()
    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

    audio_path = os.path.join(os.getcwd(), 'audio_tmp', uuid.uuid4().hex + '.wav')
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file(audio_path)
    return audio_path


if __name__ == '__main__':
    text = "我们来看看下面的内容，我们已经了解了两个数加减的奇偶性，我现在再问，奇加奇加奇，这三个数的怎么去记呀，你知道么？我们也可以把它转化成两个去记，你知道奇加奇等于偶，你一个孤单的，你一个孤单的，我们一凑就变成偶了，然后偶再加上个奇，于是我们就知道了，这个结果应该是奇数，因为一个偶数一个奇数，两者奇偶性不同。"
    # audio_path = os.path.join(os.getcwd(), uuid.uuid4().hex + '.wav')
    # stream = gen_audio(text)
    # stream.save_to_wav_file(audio_path)

    # audio_buffer = bytearray()
    # stream = gen_audio(text)
    # num = stream.read_data(audio_buffer=audio_buffer)
    # print(num)
    # print(audio_buffer)
