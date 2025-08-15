
import threading
import time
import re
import json
from dataclasses import dataclass, field
from typing import List, Dict, Generator, Callable, Any
from datetime import datetime

# デコレータ
def timer(func: Callable) -> Callable:
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f"{func.__name__} 実行時間: {end - start:.4f}秒")
		return result
	return wrapper

# データクラス
@dataclass
class Person:
	name: str
	age: int
	email: str = field(default="")

	def greet(self) -> str:
		return f"こんにちは、私は{self.name}、{self.age}歳です。"

# 継承
class Employee(Person):
	employee_id: int

	def __init__(self, name: str, age: int, employee_id: int, email: str = ""):
		super().__init__(name, age, email)
		self.employee_id = employee_id

	def greet(self) -> str:
		return f"{super().greet()} 社員番号: {self.employee_id}"

# ジェネレータ
def fibonacci(n: int) -> Generator[int, None, None]:
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, a + b

# 例外処理
def safe_divide(a: float, b: float) -> float:
	try:
		return a / b
	except ZeroDivisionError:
		print("0で割ることはできません。")
		return float('inf')

# ファイル操作
def write_json(filename: str, data: Any) -> None:
	with open(filename, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=2)

def read_json(filename: str) -> Any:
	with open(filename, 'r', encoding='utf-8') as f:
		return json.load(f)

# 正規表現
def extract_emails(text: str) -> List[str]:
	return re.findall(r"[\w\.-]+@[\w\.-]+", text)

# マルチスレッド
def print_numbers():
	for i in range(5):
		print(f"スレッド: {threading.current_thread().name}, 数字: {i}")
		time.sleep(0.1)

# リスト内包表記
def squares(n: int) -> List[int]:
	return [x * x for x in range(n)]

# ラムダ
add = lambda x, y: x + y

# 日時
def now_str() -> str:
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# メイン処理
@timer
def main():
	people = [Person("田中", 30, "tanaka@example.com"), Person("佐藤", 25)]
	employees = [Employee("山田", 40, 1001, "yamada@company.com")]
	for p in people + employees:
		print(p.greet())

	print("フィボナッチ数列:", list(fibonacci(10)))
	print("10の二乗リスト:", squares(10))
	print("加算(3, 5):", add(3, 5))
	print("現在時刻:", now_str())
	print("安全な割り算(10/0):", safe_divide(10, 0))

	text = "連絡先: tanaka@example.com, yamada@company.com"
	print("抽出されたメール:", extract_emails(text))

	data = {"people": [p.__dict__ for p in people], "employees": [e.__dict__ for e in employees]}
	write_json("sample_data.json", data)
	loaded = read_json("sample_data.json")
	print("JSON読み込み結果:", loaded)

	threads = [threading.Thread(target=print_numbers, name=f"T{i}") for i in range(2)]
	for t in threads:
		t.start()
	for t in threads:
		t.join()

if __name__ == "__main__":
	main()

# ユニットテスト
def test_safe_divide():
	assert safe_divide(10, 2) == 5
	assert safe_divide(10, 0) == float('inf')

def test_extract_emails():
	s = "a@b.com, c@d.com"
	assert extract_emails(s) == ["a@b.com", "c@d.com"]

def test_fibonacci():
	assert list(fibonacci(5)) == [0, 1, 1, 2, 3]

def run_tests():
	test_safe_divide()
	test_extract_emails()
	test_fibonacci()
	print("全テスト成功")

# テスト実行（必要ならコメントアウト解除）
# run_tests()
