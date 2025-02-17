import os
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 加载环境变量
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# 检查API密钥是否已加载
api_key = os.environ.get("ZHIPUAI_KEY")

tagging_prompt = ChatPromptTemplate.from_template("""
请根据下面的文本，提取并补充旅游行程的详细信息，包括每个时间段的地点和时间安排。请注意，只提取旅游景点，推荐地，不要提取餐馆等。输出应按照以下格式：

{{"第一天": {{
    "早上": [
      {{
        "时间": "8:00-9:30",
        "地点": "天安门广场"
      }},
      {{
        "时间": "9:30-11:00",
        "地点": "毛主席纪念堂"
      }}
    ],
    "下午": [
      {{
        "时间": "13:00-16:00",
        "地点": "故宫博物院"
      }},
      {{
        "时间": "16:30-18:00",
        "地点": "景山公园"
      }}
    ],
    "晚上": [
      {{
        "时间": "18:30-20:00",
        "地点": "王府井步行街"
      }},
      {{
        "时间": "20:30-21:30",
        "地点": "天安门广场"
      }}
    ]
  }},
  "第二天": {{
    "早上": [
      {{
        "时间": "8:00-10:00",
        "地点": "颐和园"
      }},
      {{
        "时间": "10:30-12:00",
        "地点": "圆明园"
      }}
    ],
    "下午": [
      {{
        "时间": "14:00-16:30",
        "地点": "八达岭长城"
      }},
      {{
        "时间": "17:00-18:30",
        "地点": "明十三陵"
      }}
    ],
    "晚上": [
      {{
        "时间": "19:00-21:00",
        "地点": "奥林匹克公园"
      }}
    ]
  }},
  "第三天": {{
    "早上": [
      {{
        "时间": "8:00-10:00",
        "地点": "天坛公园"
      }},
      {{
        "时间": "10:30-12:00",
        "地点": "中国美术馆"
      }}
    ],
    "下午": [
      {{
        "时间": "14:00-16:00",
        "地点": "北京动物园"
      }},
      {{
        "时间": "16:30-18:00",
        "地点": "北京植物园"
      }}
    ],
    "晚上": [
      {{
        "时间": "18:30-20:00",
        "地点": "南锣鼓巷"
      }},
      {{
        "时间": "20:30-22:00",
        "地点": "什刹海"
      }}
    ]
  }}
}}

千万注意！！！只需返回JSON结果，不要有其他多余的信息

text:{input}
""")

# 配置语言模型
llm = ChatOpenAI(
    base_url="https://open.bigmodel.cn/api/paas/v4",
    api_key=api_key,
    model="glm-4",
)

# 创建链
tagging_chain = tagging_prompt | llm
