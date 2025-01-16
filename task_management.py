from collections import deque

subject = deque([f"{value}" for value in
              ["Science", "Math", "Health", "English", "Computer"]
           ])

subject.append("Newari")
subject.append("Grammar")
print(f"Subjects added: {subject}")

subject.popleft()
print(f"Removed one subject: {subject}")

subject.rotate()
print(f"Subjects rotated: {subject}")




