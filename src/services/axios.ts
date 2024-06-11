// import <
const axios = require('axios');

// >


export async function axiosFetch(url: string): Promise<any> {

   try {

      const response: any = await axios.get(url);
      return response.data;

   } catch (error) {console.log('Error: ', error, '\nUrl: ', url);}

}