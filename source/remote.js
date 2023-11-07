// import <
const axios = require('axios');
const {Octokit} = require('@octokit/rest');

// >


async function githubGet({

   pPath,
   pOwner,
   pGithub,
   pBranch,
   pRepository,
   pEncoding = 'base64',
   pErrorMessage = 'Could not find file.'

}) {

   // try (if file exists) <
   // except (then file does not exist) <
   try {

      const response = await pGithub.repos.getContent({

         path : pPath,
         ref : pBranch,
         owner : pOwner,
         repo : pRepository

      });

      return Buffer.from(response.data.content, pEncoding).toString();

   } catch (error) {return pErrorMessage;}

   // >

}


async function githubUpdate({

   pPath,
   pOwner,
   pGithub,
   pBranch,
   pContent,
   pRepository,
   pEncoding = 'base64',
   pMessage = 'This is an automated action.',
   pErrorMessage = 'Could not create or update file.'

}) {

   // try (if exists) <
   // except (then does not exist) <
   try {

      const content = JSON.stringify(pContent);
      const response = await pGithub.repos.getContent({

         path : pPath,
         ref : pBranch,
         owner : pOwner,
         repo : pRepository

      });

      await pGithub.repos.createOrUpdateFileContents({

         path : pPath,
         ref : pBranch,
         owner : pOwner,
         repo : pRepository,
         message : pMessage,
         sha : response.data.sha,
         content : Buffer.from(content).toString(pEncoding)

      });

   } catch (error) {console.log(error); return pErrorMessage;}

   // >

}


async function axiosGet({
   
   pURL,
   pErrorMessage = 'Data could not be loaded.'

}) {

   try { return (await axios.get(pURL)).data}   
   catch (error) {return pErrorMessage;}

}


// export <
module.exports = {

   axiosGet,
   githubGet,
   githubUpdate

};

// >