// import <
const axios = require('axios');

// >


async function githubGet({

   pPath,
   pOwner,
   pGithub,
   pRepository,

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

      return Buffer.from(response.data.content, opEncoding).toString('utf-8');
   
   } catch (error) {return {

      true : error,
      false : opErrorMessage

   }[opShowError];}

   // >

}


async function githubSet({

   pPath,
   pOwner,
   pGithub,
   pContent,
   pRepository,

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
         content : Buffer.from(JSON.stringify(pContent)).toString(opEncoding),
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

   pPath,
   pOwner,
   pGithub,
   pContent,
   pRepository,

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
         content : Buffer.from(JSON.stringify(pContent)).toString(opEncoding),

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