"""
Multilingual BMI Calculator / Kalkulator IMT / BMI計算機
Languages: English, Bahasa Indonesia, & 日本語 (Japanese)
Supports both Imperial (English) units and Metric units.
"""

import sys
from typing import Tuple, Dict, Any

# Ensure UTF-8 output encoding across Windows console environments
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if hasattr(sys.stdin, "reconfigure"):
    try:
        sys.stdin.reconfigure(encoding="utf-8")
    except Exception:
        pass

TRANSLATIONS: Dict[str, Dict[str, Any]] = {
    "en": {
        "app_title": "BMI CALCULATOR (BODY MASS INDEX)",
        "menu_prompt": "Please choose an option:",
        "opt_imperial": "1) English / Imperial Units (Pounds, Feet & Inches)",
        "opt_metric": "2) Metric Units (Kilograms, Centimeters)",
        "opt_change_lang": "3) Change Language / Ganti Bahasa / 言語を変更",
        "opt_exit": "4) Exit",
        "choice_prompt": "Enter your choice (1-4): ",
        "invalid_choice": "[!] Invalid selection. Please enter a number between 1 and 4.",
        "imperial_header": "--- English / Imperial Units ---",
        "height_format_prompt": "Height input format:\n  1) Feet and Inches (e.g., 5 ft 10 in)\n  2) Total Inches (e.g., 70 in)\nSelect format [1 or 2, default: 1]: ",
        "enter_total_inches": "Enter total height in inches: ",
        "enter_feet": "Enter height - feet: ",
        "enter_inches_part": "Enter height - inches [0-11]: ",
        "invalid_inches_range": "  [!] Inches should be between 0 and 11.99.",
        "enter_weight_lbs": "Enter weight in pounds (lbs): ",
        "metric_header": "--- Metric Units ---",
        "enter_height_cm": "Enter height in centimeters (cm): ",
        "enter_weight_kg": "Enter weight in kilograms (kg): ",
        "error_positive": "  [!] Please enter a positive number greater than 0.",
        "error_number": "  [!] Invalid input. Please enter a valid number.",
        "report_title": "BMI REPORT",
        "label_bmi": "Your BMI",
        "label_category": "Category",
        "label_healthy_range": "Healthy Weight Range",
        "label_note": "Health Note",
        "unit_lbs": "lbs",
        "unit_kg": "kg",
        "goodbye": "Thank you for using BMI Calculator. Stay healthy and goodbye!",
        "categories": {
            "underweight": {
                "name": "Underweight",
                "advice": "You may need to gain weight. Consult a healthcare provider or nutritionist for personalized guidance."
            },
            "normal": {
                "name": "Normal weight",
                "advice": "You are in a healthy weight range for your height. Keep up the balanced lifestyle!"
            },
            "overweight": {
                "name": "Overweight",
                "advice": "You are slightly above the typical healthy weight range. Consider regular physical activity and a balanced diet."
            },
            "obese_1": {
                "name": "Obesity (Class I)",
                "advice": "Your BMI falls into Obesity Class I. Consulting a doctor or registered dietitian is recommended."
            },
            "obese_2": {
                "name": "Obesity (Class II)",
                "advice": "Your BMI falls into Obesity Class II. Medical consultation is strongly advised."
            },
            "obese_3": {
                "name": "Severe / Morbid Obesity (Class III)",
                "advice": "Your BMI falls into Obesity Class III. Please consult a healthcare professional for clinical guidance."
            },
        }
    },
    "id": {
        "app_title": "KALKULATOR IMT / BMI (INDEKS MASSA TUBUH)",
        "menu_prompt": "Silakan pilih menu:",
        "opt_imperial": "1) Satuan Imperial / Inggris (Pound, Kaki & Inci)",
        "opt_metric": "2) Satuan Metrik (Kilogram, Sentimeter)",
        "opt_change_lang": "3) Ganti Bahasa / Change Language / 言語を変更",
        "opt_exit": "4) Keluar",
        "choice_prompt": "Masukkan pilihan Anda (1-4): ",
        "invalid_choice": "[!] Pilihan tidak valid. Silakan masukkan angka antara 1 dan 4.",
        "imperial_header": "--- Satuan Imperial / Inggris ---",
        "height_format_prompt": "Format input tinggi badan:\n  1) Kaki dan Inci (contoh: 5 kaki 10 inci)\n  2) Total Inci (contoh: 70 inci)\nPilih format [1 atau 2, default: 1]: ",
        "enter_total_inches": "Masukkan total tinggi badan dalam inci: ",
        "enter_feet": "Masukkan tinggi badan - kaki (feet): ",
        "enter_inches_part": "Masukkan tinggi badan - inci [0-11]: ",
        "invalid_inches_range": "  [!] Inci harus berada di antara 0 dan 11.99.",
        "enter_weight_lbs": "Masukkan berat badan dalam pound (lbs): ",
        "metric_header": "--- Satuan Metrik ---",
        "enter_height_cm": "Masukkan tinggi badan dalam sentimeter (cm): ",
        "enter_weight_kg": "Masukkan berat badan dalam kilogram (kg): ",
        "error_positive": "  [!] Harap masukkan angka positif lebih dari 0.",
        "error_number": "  [!] Masukan tidak valid. Harap masukkan angka yang benar.",
        "report_title": "LAPORAN HASIL IMT / BMI",
        "label_bmi": "Nilai IMT / BMI Anda",
        "label_category": "Kategori",
        "label_healthy_range": "Rentang Berat Badan Ideal",
        "label_note": "Catatan Kesehatan",
        "unit_lbs": "lbs (pon)",
        "unit_kg": "kg",
        "goodbye": "Terima kasih telah menggunakan Kalkulator IMT. Jaga selalu kesehatan Anda!",
        "categories": {
            "underweight": {
                "name": "Berat Badan Kurang (Underweight)",
                "advice": "Berat badan Anda di bawah batas ideal. Konsultasikan dengan dokter atau ahli gizi untuk menambah berat badan secara sehat."
            },
            "normal": {
                "name": "Berat Badan Normal / Ideal",
                "advice": "Berat badan Anda berada dalam kisaran sehat dan ideal. Pertahankan pola makan seimbang dan gaya hidup aktif!"
            },
            "overweight": {
                "name": "Kelebihan Berat Badan (Overweight)",
                "advice": "Berat badan Anda melebihi kisaran ideal. Pertimbangkan untuk berolahraga secara teratur dan menjaga pola makan sehat."
            },
            "obese_1": {
                "name": "Obesitas (Tingkat I)",
                "advice": "IMT Anda masuk dalam kategori Obesitas Tingkat I. Disarankan untuk berkonsultasi dengan dokter atau ahli gizi."
            },
            "obese_2": {
                "name": "Obesitas (Tingkat II)",
                "advice": "IMT Anda masuk dalam kategori Obesitas Tingkat II. Sangat disarankan untuk memeriksakan kesehatan ke dokter."
            },
            "obese_3": {
                "name": "Obesitas Parah / Morbid (Tingkat III)",
                "advice": "IMT Anda masuk dalam kategori Obesitas Tingkat III. Harap segera konsultasikan dengan profesional medis."
            },
        }
    },
    "ja": {
        "app_title": "BMI 計算機（体格指数）",
        "menu_prompt": "オプションを選択してください:",
        "opt_imperial": "1) ヤード・ポンド法（ポンド、フィート・インチ）",
        "opt_metric": "2) メートル法（キログラム、センチメートル）",
        "opt_change_lang": "3) 言語を変更 / Change Language / Ganti Bahasa",
        "opt_exit": "4) 終了",
        "choice_prompt": "選択肢を入力してください (1-4): ",
        "invalid_choice": "[!] 選択が無効です。1から4の数値を入力してください。",
        "imperial_header": "--- ヤード・ポンド法 ---",
        "height_format_prompt": "身長の入力形式:\n  1) フィートとインチ（例: 5フィート 10インチ）\n  2) 合計インチ（例: 70インチ）\n形式を選択 [1 または 2, デフォルト: 1]: ",
        "enter_total_inches": "合計身長をインチで入力してください: ",
        "enter_feet": "身長 - フィート (feet) を入力してください: ",
        "enter_inches_part": "身長 - インチ (inches) [0-11] を入力してください: ",
        "invalid_inches_range": "  [!] インチは0から11.99の間で入力してください。",
        "enter_weight_lbs": "体重をポンド (lbs) で入力してください: ",
        "metric_header": "--- メートル法 ---",
        "enter_height_cm": "身長をセンチメートル (cm) で入力してください: ",
        "enter_weight_kg": "体重をキログラム (kg) で入力してください: ",
        "error_positive": "  [!] 0より大きい正の数値を入力してください。",
        "error_number": "  [!] 入力が無効です。有効な数値を入力してください。",
        "report_title": "BMI 測定レポート",
        "label_bmi": "あなたのBMI",
        "label_category": "判定区分",
        "label_healthy_range": "適正体重の範囲",
        "label_note": "健康アドバイス",
        "unit_lbs": "ポンド (lbs)",
        "unit_kg": "kg",
        "goodbye": "BMI計算機をご利用いただきありがとうございました。健康にお過ごしください！",
        "categories": {
            "underweight": {
                "name": "低体重（痩せ型）",
                "advice": "体重が適正範囲を下回っています。必要に応じて医師や管理栄養士にご相談の上、健康的に体重を増やすことをおすすめします。"
            },
            "normal": {
                "name": "普通体重（標準）",
                "advice": "身長に対して健康的な体重です。引き続きバランスの取れた食事と適度な運動を心がけましょう！"
            },
            "overweight": {
                "name": "肥満（1度） / 過体重",
                "advice": "標準体重をやや上回っています。適度な運動と食生活の見直しを検討してみてください。"
            },
            "obese_1": {
                "name": "肥満（2度）",
                "advice": "BMIが肥満2度に該当します。生活習慣の改善や専門医への相談をおすすめします。"
            },
            "obese_2": {
                "name": "肥満（3度）",
                "advice": "BMIが肥満3度に該当します。健康障害リスクを減らすため、医師の診察を強く推奨します。"
            },
            "obese_3": {
                "name": "肥満（4度 / 高度肥満）",
                "advice": "高度の肥満に該当します。医療機関を受診し、適切な治療・指導を受けることをおすすめします。"
            },
        }
    }
}


def calculate_bmi_imperial(weight_lbs: float, height_inches: float) -> float:
    """Calculate BMI using Imperial / English units.
    Formula: (weight in lbs / (height in inches)^2) * 703
    """
    if height_inches <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_lbs <= 0:
        raise ValueError("Weight must be greater than zero.")
    return (weight_lbs / (height_inches ** 2)) * 703


def calculate_bmi_metric(weight_kg: float, height_cm: float) -> float:
    """Calculate BMI using Metric units.
    Formula: weight in kg / (height in meters)^2
    """
    if height_cm <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    height_m = height_cm / 100.0
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi: float, lang: str = "en") -> Tuple[str, str]:
    """Return the BMI category and advice according to selected language ('en', 'id', or 'ja')."""
    cats = TRANSLATIONS[lang]["categories"]
    if bmi < 18.5:
        data = cats["underweight"]
    elif 18.5 <= bmi < 25.0:
        data = cats["normal"]
    elif 25.0 <= bmi < 30.0:
        data = cats["overweight"]
    elif 30.0 <= bmi < 35.0:
        data = cats["obese_1"]
    elif 35.0 <= bmi < 40.0:
        data = cats["obese_2"]
    else:
        data = cats["obese_3"]
    return data["name"], data["advice"]


def get_healthy_weight_range_imperial(height_inches: float) -> Tuple[float, float]:
    """Calculate healthy weight range (BMI 18.5 to 24.9) in pounds for given height in inches."""
    min_weight = (18.5 * (height_inches ** 2)) / 703
    max_weight = (24.9 * (height_inches ** 2)) / 703
    return min_weight, max_weight


def get_healthy_weight_range_metric(height_cm: float) -> Tuple[float, float]:
    """Calculate healthy weight range (BMI 18.5 to 24.9) in kg for given height in cm."""
    height_m = height_cm / 100.0
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return min_weight, max_weight


def prompt_positive_float(prompt_message: str, error_pos: str, error_num: str) -> float:
    """Prompt until a positive float is entered."""
    while True:
        user_input = input(prompt_message).strip()
        try:
            val = float(user_input)
            if val <= 0:
                print(error_pos)
                continue
            return val
        except ValueError:
            print(error_num)


def display_results(
    bmi: float,
    category: str,
    advice: str,
    healthy_min: float,
    healthy_max: float,
    unit_label: str,
    t: Dict[str, Any]
):
    """Print the calculated BMI report."""
    border = "=" * 60
    print("\n" + border)
    print(f"                 {t['report_title']}")
    print(border)
    print(f"  {t['label_bmi']:<25}: {bmi:.2f}")
    print(f"  {t['label_category']:<25}: {category}")
    print(f"  {t['label_healthy_range']:<25}: {healthy_min:.1f} - {healthy_max:.1f} {unit_label}")
    print("-" * 60)
    print(f"  {t['label_note']}:")
    print(f"  {advice}")
    print(border + "\n")


def run_imperial_flow(lang: str):
    """Run flow for English / Imperial units."""
    t = TRANSLATIONS[lang]
    print(f"\n{t['imperial_header']}")
    choice = input(t["height_format_prompt"]).strip()

    if choice == "2":
        height_inches = prompt_positive_float(
            t["enter_total_inches"], t["error_positive"], t["error_number"]
        )
    else:
        feet = prompt_positive_float(
            t["enter_feet"], t["error_positive"], t["error_number"]
        )
        while True:
            inches_input = input(t["enter_inches_part"]).strip()
            try:
                inches = float(inches_input)
                if 0 <= inches < 12:
                    break
                print(t["invalid_inches_range"])
            except ValueError:
                print(t["error_number"])
        height_inches = (feet * 12) + inches

    weight_lbs = prompt_positive_float(
        t["enter_weight_lbs"], t["error_positive"], t["error_number"]
    )

    bmi = calculate_bmi_imperial(weight_lbs, height_inches)
    category, advice = get_bmi_category(bmi, lang)
    min_w, max_w = get_healthy_weight_range_imperial(height_inches)
    display_results(bmi, category, advice, min_w, max_w, t["unit_lbs"], t)


def run_metric_flow(lang: str):
    """Run flow for Metric units."""
    t = TRANSLATIONS[lang]
    print(f"\n{t['metric_header']}")
    height_cm = prompt_positive_float(
        t["enter_height_cm"], t["error_positive"], t["error_number"]
    )
    weight_kg = prompt_positive_float(
        t["enter_weight_kg"], t["error_positive"], t["error_number"]
    )

    bmi = calculate_bmi_metric(weight_kg, height_cm)
    category, advice = get_bmi_category(bmi, lang)
    min_w, max_w = get_healthy_weight_range_metric(height_cm)
    display_results(bmi, category, advice, min_w, max_w, t["unit_kg"], t)


def choose_language() -> str:
    """Prompt user to select English, Bahasa Indonesia, or Japanese."""
    print("\n------------------------------------------------------------")
    print(" Select Language / Pilih Bahasa / 言語を選択:")
    print("   1) English")
    print("   2) Bahasa Indonesia")
    print("   3) 日本語 (Japanese)")
    print("------------------------------------------------------------")
    while True:
        sel = input("Choice / Pilihan / 選択 [1, 2, or 3, default: 1]: ").strip()
        if sel in ("1", ""):
            return "en"
        elif sel == "2":
            return "id"
        elif sel == "3":
            return "ja"
        print("[!] Please enter 1 for English, 2 for Bahasa Indonesia, or 3 for Japanese.")


def main():
    print("=" * 60)
    print("  BMI CALCULATOR / KALKULATOR IMT / BMI計算機")
    print("=" * 60)

    lang = choose_language()

    while True:
        t = TRANSLATIONS[lang]
        border = "=" * 60
        print("\n" + border)
        print(f"  {t['app_title']}")
        print(border)
        print(t["menu_prompt"])
        print(f"  {t['opt_imperial']}")
        print(f"  {t['opt_metric']}")
        print(f"  {t['opt_change_lang']}")
        print(f"  {t['opt_exit']}")

        choice = input("\n" + t["choice_prompt"]).strip()

        if choice == "1":
            run_imperial_flow(lang)
        elif choice == "2":
            run_metric_flow(lang)
        elif choice == "3":
            lang = choose_language()
        elif choice == "4":
            print(f"\n{t['goodbye']}\n")
            break
        else:
            print(f"\n{t['invalid_choice']}\n")


if __name__ == "__main__":
    main()
