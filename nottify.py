from plyer import notification

notification.notify(
    title="Reminder",
    message="Take a break and drink water!",
    app_name="Python Reminder",
    timeout=10
)

print("Notification sent successfully!")