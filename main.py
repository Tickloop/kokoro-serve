from uuid import uuid4
from fastapi import FastAPI, Body
from fastapi.responses import StreamingResponse

from kokoro import KPipeline
import soundfile as sf
import asyncio

import torch

app = FastAPI()
pipeline = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")


@app.get("/voices")
async def get_voices():
    # https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
    voices = (
        "af_alloy,af_aoede,af_bella,af_heart,af_jessica,af_kore,af_nicole,af_nova,af_river,af_sarah,af_sky,"
        "am_adam,am_echo,am_eric,am_fenrir,am_liam,am_michael,am_onyx,am_puck,am_santa,bf_alice,bf_emma,bf_isabella,"
        "bf_lily,bm_daniel,bm_fable,bm_george,bm_lewis,ef_dora,em_alex,em_santa,ff_siwis,hf_alpha,hf_beta,hm_omega,"
        "hm_psi,if_sara,im_nicola,jf_alpha,jf_gongitsune,jf_nezumi,jf_tebukuro,jm_kumo,pf_dora,pm_alex,pm_santa,"
        "zf_xiaobei,zf_xiaoni,zf_xiaoxiao,zf_xiaoyi,zm_yunjian,zm_yunxi,zm_yunxia,zm_yunyang"
    )
    return {"voices": voices.split(",")}


@app.post("/generate")
async def generate(
    text: str = Body(description="Input text to be synthesized"),
    voice: str = Body(description="Voice to be used for synthesis"),
) -> StreamingResponse:
    audio_data = torch.zeros(1)
    generator = await asyncio.to_thread(pipeline, text, voice=voice, split_pattern=None)
    for _, _, audio in generator:
        if isinstance(audio, torch.FloatTensor):
            audio_data = torch.cat((audio_data, audio), dim=-1)
    output_filename = f"/tmp/{uuid4()}.wav"
    await asyncio.to_thread(sf.write, output_filename, audio_data, samplerate=24000)
    return StreamingResponse(
        open(output_filename, "rb"),
        media_type="application/x-wav",
        headers={"Content-Disposition": f"attachment; filename={output_filename}"},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, workers=1)
