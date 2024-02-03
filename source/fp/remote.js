// import <
const axios = require('axios');

// >


async function githubGet({

   pPath,
   pOwner,
   pGithub,
   pRepository,

   opParse = false,
   opBranch = 'main',
   opShowError = false,
   opEncoding = 'base64',
   opErrorMessage = 'Could not locate file.'

}) {

   // try (if ) <
   // except (then ) <
   try {

      const response = await pGithub.request('GET /repos/{owner}/{repo}/contents/{path}', {

         path : pPath,
         ref : opBranch,
         owner : pOwner,
         repo : pRepository

      });

      let result = Buffer.from(response.data.content, opEncoding).toString('utf-8');

      return {

         false : result,
         true : JSON.parse(result)

      }[opParse];
   
   } catch (error) {return {

      true : error,
      false : opErrorMessage

   }[opShowError];}

   // >

}


async function githubSet({

   pData,
   pPath,
   pOwner,
   pGithub,
   pRepository,

   opSpacer = 3,
   opBranch = 'main',
   opShowError = true,
   opEncoding = 'base64',
   opName = 'Alex Arbuckle',
   opEmail = 'lxrbckl@gmail.com',
   opMessage = 'Automated Action',
   opErrorMessage = 'Could not set file.'

}) {

   // try (if ) <
   // except (then ) <
   try {

      await pGithub.request('PUT /repos/{owner}/{repo}/contents/{path}', {

         path : pPath,
         owner : pOwner,
         branch : opBranch,
         repo : pRepository,
         message : opMessage,
         content : Buffer.from(JSON.stringify(pData, null, opSpacer)).toString(opEncoding),
         committer : {

            name : opName,
            email : opEmail

         }

      });

   } catch (error) {return {

      true : error,
      false : opErrorMessage

   }[opShowError];}

   // >

}


async function githubUpdate({

   pData,
   pPath,
   pOwner,
   pGithub,
   pRepository,

   opSpacer = 3,
   opBranch = 'main',
   opShowError = true,
   opEncoding = 'base64',
   opMessage = 'Automated Action',
   opErrorMessage = 'Could not update file.'

}) {

   try {

      const response = await pGithub.request('GET /repos/{owner}/{repo}/contents/{path}', {

         path : pPath,
         ref : opBranch,
         owner : pOwner,
         repo : pRepository

      });
      await pGithub.request('PUT /repos/{owner}/{repo}/contents/{path}', {

         path : pPath,
         owner : pOwner,
         branch : opBranch,
         repo : pRepository,
         message : opMessage,
         sha : response.data.sha,
         content : Buffer.from(JSON.stringify(pData, null, opSpacer)).toString(opEncoding),

      });
   
   } catch (error) {return {

      true : error,
      false : opErrorMessage

   }[opShowError];}

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
   githubSet,
   githubUpdate

};

// >