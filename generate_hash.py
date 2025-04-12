from werkzeug.security import generate_password_hash

# 输入你的密码
password = "Wenxiu1234*"

# 生成哈希
hashed_password = generate_password_hash(password)

print("Generated Password Hash:")
print(hashed_password)