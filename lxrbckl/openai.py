# import <
from openai import AsyncOpenAI

# >


class openai:
   
   def __init__(
      
      self, 
      token,
      
      role = 'user',
      model = 'gpt-4o',
      temperature = 1.5
   
   ):
      '''  '''
      
      self.role = role
      self.model = model
      self.temperature = temperature
      
      self.openai = AsyncOpenAI(api_key = token)

      
   async def message(
      
      self,
      content
      
   ):
      '''  '''
      
      reply = await self.openai.chat.completions.create(
         
         model = self.model,
         temperature = self.temperature,
         messages = [{"role" : self.role, "content" : content}]
         
      )
      
      return reply.choices[0].message.content