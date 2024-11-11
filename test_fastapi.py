from fastapi import BackgroundTasks, FastAPI  # import BackgroundTasks
from pydantic import BaseModel


class Data(BaseModel):
    data: str

app = FastAPI()

# define background task
def write_log(message: str):
    with open("log.txt", "a") as log:
        log.write(f"{message}\n")

@app.post("/submit-data/")
@app.middleware("http")
async def submit_data(data: Data, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Data received: {data.data}") # add task to queue
    return {"message": "Data is being processed in the background."}



list_with_duplicates = [5, 2, 2, 4, 4, 1, 3, 5]
print(dict.fromkeys(list_with_duplicates))
# remove duplicates while preserving list order
list_without_duplicates = list(dict.fromkeys(list_with_duplicates))
print(list_without_duplicates)
# will print [5, 2, 4, 1, 3]
