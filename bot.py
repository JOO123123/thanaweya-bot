from datetime import datetime
import os
import random
import requests

exam_date = datetime(2027, 6, 1)
today = datetime.now()
remaining_days = (exam_date - today).days

intros = [
    "يا رجالة، محمد عبد اللطيف بيقولكم",
    "يا أبطال، معاكوا محمد عبد اللطيف و",
    "اصحوا للكلام مع محمد عبد اللطيف،",
    "يا عتاولة، محمد عبد اللطيف بيفكركم إن",
    "يا شباب، كلمة سر النهاردة من محمد عبد اللطيف:",
    "صباح الفل يا رجالة، محمد عبد اللطيف بيصبح وبيقسملكم إن",
    "يا رجالة ثانوية 2027، محمد عبد اللطيف بيقول:",
    "شدوا حيلكم يا رجالة، محمد عبد اللطيف شايف إن",
]

middles = [
    f"فاضل {remaining_days} يوم علي امتحانات ثانوية عامة 2027.. لسه شفت حاجة ده لسه الجد ما بداش!",
    f"العد التنازلي شغال ومش مستني حد، فاضل {remaining_days} يوم بالظبط!",
    (
        f"باقي {remaining_days} يوم بس.. اضرب الطوب بالنار ووريني شطارتك"
        " الفترة دي!"
    ),
    (
        f"فاضل {remaining_days} يوم.. اللعب خلص والشغل الجدي بدأ يا رجالة."
    ),
    (
        f"الأيام بتجري، فاضل {remaining_days} يوم علي الحلم الكبير، اصحى!"
    ),
    (
        f"مفيش وقت للكسل، فاضل {remaining_days} يوم وخلي روحك عالية دايماً."
    ),
    (
        f"يا ناس اصحوا، فاضل {remaining_days} يوم علي الامتحانات، الميدان"
        " ياناس!"
    ),
]

day_seed = today.day + today.month * 30 + today.year * 365
random.seed(day_seed)

selected_intro = random.choice(intros)
selected_middle = random.choice(middles)

# روابط GIFs مباشرة ومضمونة تظهر كصور متحركة في ديسكورد مباشرة
gifs = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd21rend4cmQ3djVoYTlqc2IyNGZmNHh1MDRjbno2Y3I0M3B0MGp6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xT39CVxQ2yz9gEdLyM/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd21rend4cmQ3djVoYTlqc2IyNGZmNHh1MDRjbno2Y3I0M3B0MGp6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26ufouiy09sRIZSCY/giphy.gif",
    "https://media.giphy.com/media/3o7TKSjRrfIPjeiOkM/giphy.gif",
    "https://media.giphy.com/media/l0HlRnAWXxn0MhOBK/giphy.gif",
    "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",
]

selected_gif = random.choice(gifs)

# استخدام الـ embeds عشان تظهر الصورة متحركة بشكل نظيف بدون لينكات نصية
payload = {
    "content": (
        f"🚨 **رسالة اليوم من محمد عبد اللطيف** 🚨\n\n{selected_intro}"
        f" {selected_middle}\n\n*هذا الحساب لا يمط للحقيقة بصلة*"
    ),
    "embeds": [{"image": {"url": selected_gif}}],
}

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

if webhook_url:
  response = requests.post(webhook_url, json=payload)
  print(f"Status Code: {response.status_code}")
else:
  print("Webhook URL not found!")
