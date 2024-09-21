import tasks.demo_task as demo_task
from utils import get_website_status

def main():
    print("Running demo task...")
    demo_task.run_demo()

    url = "https://www.example.com"
    status = get_website_status(url)
    print(f"Website status of {url} is {status}")

if __name__ == "__main__":
    main()
