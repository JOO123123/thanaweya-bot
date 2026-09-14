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

# روابط صور متحركة مباشرة بصيغة .gif بتظهر فوراً كصورة في ديسكورد
gifs = [
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZkdnA2YWV3OHFzZDV4aTZidXZ3MndwbjQ0N20ybHZqcThsdzlyZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjRrfIPjeiOkM/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJqanl6amF2ZXJtMGprNWN5NGV6ZXU2cG9vdmZ3d2d2cWl3OWl4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26ufdipQqU2lhNA4g/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNndmbXlnZm91N2Rnb3MyMHRhbXJ4d2J5OXB3dXg4Ymd0Z2N6MWRlayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0HlRnAWXxn0MhOBK/giphy.gif",
]

selected_gif = random.choice(gifs)

# الطريقة دي بتضمن إن الصورة تظهر كـ Embed حقيقي جوه الرسالة من غير لينكات نصية
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
