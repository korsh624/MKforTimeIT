# predict_app.py
import joblib

model = joblib.load('student_model.pkl')

print("Введите данные для прогноза:")
grade = float(input("Средний балл (0–5): "))
hours = int(input("Количество внеурочных часов: "))
olymp = int(input("Количество олимпиад: "))

prediction = model.predict([[grade, hours, olymp]])
print("\nРезультат:")
if prediction[0] == 1:
    print("✅ Высока вероятность, что студент поступит!")
else:
    print("❌ Модель считает, что шансы невелики.")
