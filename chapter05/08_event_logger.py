from datetime import datetime

def log_event(event_type: str, **kwargs: dict) -> None:
    print(f"Event type: {event_type}")
    timestamp =datetime.now().isoformat()
    print(f"Timestamp: {timestamp}")

    for key, value in kwargs.items():
        print(f"{key} : {value}")

def main():
    log_event("UserLogin", user="johnDoe", status="Success", ip="192.168.1.1\n")
    log_event("FileUpload", user="johnDoe", status="Failure", filename="report.pdf", reason="File too large", ip="192.168.1.1\n")

if __name__ == "__main__":
    main()
