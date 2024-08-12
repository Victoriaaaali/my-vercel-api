from fastapi import FastAPI, File, UploadFile
from gradio_client import Client, file

app = FastAPI()
client = Client("tonyassi/voice-clone")

@app.post("/voice-clone/")
async def clone_voice(text: str, audio: UploadFile = File(...)):
    # Guarda el archivo de audio en la memoria o en un directorio temporal
    audio_path = f"/tmp/{audio.filename}"
    with open(audio_path, "wb") as f:
        f.write(await audio.read())
    
    # Llama al modelo de Hugging Face
    result = client.predict(
        text=text,
        audio=file(audio_path),
        api_name="/predict"
    )
    
    # Retorna el resultado
    return {"output_audio": result}
