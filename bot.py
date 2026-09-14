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

# جفاتك الأصلية كاملة
gifs = [
    "https://qasrelmemez.com/meme/892f4b70-c217-4c49-9a84-51f69e3f4f31",
    "https://qasrelmemez.com/meme/8f330a82-2e8f-4068-b62e-f4c241a1cf98",
    "https://qasrelmemez.com/meme/dab3bb24-eda9-42be-8d34-5f931c00d0c5",
    "https://qasrelmemez.com/meme/ca83e655-0d83-4420-b14e-b77564a15821",
    "https://qasrelmemez.com/meme/960b00b4-8515-41d5-8924-cb3da64d68d0",
    "https://qasrelmemez.com/meme/29f76493-7da3-4e65-be23-97b2d97eb7e2",
    "https://qasrelmemez.com/meme/35cdd4a3-9dda-4df7-8da6-8ce5bb84f50c",
    "https://qasrelmemez.com/meme/7aa260fd-81b6-4bff-9e1a-54f625062c76",
    "https://qasrelmemez.com/meme/95b46127-5011-438f-ac03-e333a959e688",
    "https://qasrelmemez.com/meme/3294c46a-befe-4025-8ea8-2d7c2864d215",
    "https://qasrelmemez.com/meme/817d04b8-8649-42d4-8887-9d1e0ddfbed7",
    "https://qasrelmemez.com/meme/918aeb49-52b6-4f89-8d5c-5011592136ba",
    "https://qasrelmemez.com/meme/9553509e-b1fc-4389-a783-76022316e185",
    "https://qasrelmemez.com/meme/d15a7fd5-9657-48a1-88e0-05587c973e68",
    "https://qasrelmemez.com/meme/2ba82643-31ba-467c-b2ff-e5ae78bc758b",
    "https://qasrelmemez.com/meme/57106949-45cc-4d3e-890d-c186f05fd023",
    "https://qasrelmemez.com/meme/33ee60e2-5b46-4753-98a9-aa2eda183be4",
    "https://qasrelmemez.com/meme/c91856dc-b188-4eca-8ca2-7b0d7896445e",
    "https://qasrelmemez.com/meme/f9218848-0803-4851-ba10-ef062f7938fa",
    "https://qasrelmemez.com/meme/01ec7fc8-cc22-414c-8ffd-5ee9595efe3d",
    "https://qasrelmemez.com/meme/cbcde946-5e12-48ac-b49b-604b7e0fa3c0",
    "https://qasrelmemez.com/meme/abbf2426-eaf4-49b7-8a5f-4465b58b6327",
    "https://qasrelmemez.com/meme/482eb681-ab0a-416d-952a-89c4488268ed",
    "https://qasrelmemez.com/meme/bc93499c-c991-4581-b23b-62f9fc886bde",
    "https://qasrelmemez.com/meme/f07fb2b0-6b2b-468b-920c-665956c04547",
    "https://qasrelmemez.com/meme/8edc62f5-c395-4206-91ba-e59a0756c50f",
    "https://qasrelmemez.com/meme/93279311-c249-464a-a6a1-2a957e2b806c",
    "https://qasrelmemez.com/meme/a124ab0d-fbdc-4161-a76f-2d54000ccd23",
    "https://qasrelmemez.com/meme/d2a3563f-2116-4500-afc3-77caf090805d",
    "https://qasrelmemez.com/meme/4c59c658-e964-49ce-9c66-df02fa73b831",
    "https://qasrelmemez.com/meme/6f956f7e-f17d-4daa-9d14-ddfdabb7c8f6",
    "https://qasrelmemez.com/meme/8f84e567-a279-4ff2-b57c-c6ad8b632c05",
]

selected_gif = random.choice(gifs)

# اللينك هيظهر عادي جداً زي ما طلبت
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
