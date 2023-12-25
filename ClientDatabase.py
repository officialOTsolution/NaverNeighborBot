from pymongo import MongoClient
from bson import ObjectId
import hashlib

# MongoDB 연결 설정
client = MongoClient("mongodb://localhost:27017")
db = client["your_database_name"]
collection = db["your_collection_name"]

def authenticate_user(username, password):
    # 입력된 비밀번호를 해싱하여 저장된 비밀번호와 비교
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # MongoDB에서 유저 정보 조회
    user = collection.find_one({"username": username, "password": hashed_password})

    if user:
        print("인증 성공!")
    else:
        print("인증 실패.")

# 테스트용 입력
username_input = input("아이디를 입력하세요: ")
password_input = input("비밀번호를 입력하세요: ")

# 유저 인증 함수 호출
authenticate_user(username_input, password_input)