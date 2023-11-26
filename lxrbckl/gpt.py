# import <
from openai import AsyncOpenAI

# >


class gpt:
   
   def __init__(self, token):
      '''  '''
      
      self.openai = AsyncOpenAI(api_key = token)

      
   async def message(
      
      self,
      message,
      
      role = 'user',
      model = 'gpt-3.5-turbo'
      
   ):
      '''  '''
      
      chat = await self.openai.chat.completions.create(
         
         model = model,
         messages = [{
            
            "role" : role,
            "content" : message
            
         }]
         
      )
      
      return chat.choices[0].message.content