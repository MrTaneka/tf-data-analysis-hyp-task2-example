import pandas as pd
import numpy as np

chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.08
    xm=x.mean()
    ym=y.mean()
    xd=x.var()
    yd=y.var()

    ans=abs((xm-ym)/(np.sqrt(xd+yd)))
    result = False
    if ans < alpha:
      result = True
    
    return result # Ваш ответ, True или False
