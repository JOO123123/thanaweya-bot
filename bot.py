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

# لينكات Giphy الأصلية اللي ديسكورد بيعرف يعملها Embed لوحده تلقائياً
gifs = [
    "https://giphy.com/gifs/xT39CVxQ2yz9gEdLyM",
    "https://giphy.com/gifs/26ufouiy09sRIZSCY",
    "https://giphy.com/gifs/3o7TKSjRrfIPjeiOkM",
    "https://giphy.com/gifs/l0HlRnAWXxn0MhOBK",
    "https://giphy.com/gifs/26ufdipQqU2lhNA4g",
]

selected_gif = random.choice(gifs)

payload = {
    "content": (
        f"🚨 **رسالة اليوم من محمد عبد اللطيف** 🚨\n\n{selected_intro}"
        f" {selected_middle}\n\n{selected_gif}\n\n*هذا الحساب لا يمط للحقيقة"
        " بصلة*"
    )
}

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

if webhook_url:
  response = requests.post(webhook_url, json=payload)
  print(f"Status Code: {response.status_code}")
else:
  print("Webhook URL not found!")
