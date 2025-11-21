# to cache the model download from HF on first import and all avialble voices as of 21st Nov 2025
from kokoro import KPipeline
print("=" * 40, "Caching Kokoro model and voices", "=" * 40)
pipeline = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
voices = 'af_alloy,af_aoede,af_bella,af_heart,af_jessica,af_kore,af_nicole,af_nova,af_river,af_sarah,af_sky,am_adam,am_echo,am_eric,am_fenrir,am_liam,am_michael,am_onyx,am_puck,am_santa,bf_alice,bf_emma,bf_isabella,bf_lily,bm_daniel,bm_fable,bm_george,bm_lewis,ef_dora,em_alex,em_santa,ff_siwis,hf_alpha,hf_beta,hm_omega,hm_psi,if_sara,im_nicola,jf_alpha,jf_gongitsune,jf_nezumi,jf_tebukuro,jm_kumo,pf_dora,pm_alex,pm_santa,zf_xiaobei,zf_xiaoni,zf_xiaoxiao,zf_xiaoyi,zm_yunjian,zm_yunxi,zm_yunxia,zm_yunyang'
for voice in voices.split(','):
    pipeline.load_single_voice(voice=voice)