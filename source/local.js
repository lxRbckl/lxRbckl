// import <
const fs = require('fs').promises;
const path = require('path');

// >


function getProjectPath(
   
   pFile = '',
   pDelimeter = '/'
   
) {

   const dir = path.dirname(__filename);
   const file = pFile.split(/[/\\]/).join(pDelimeter);

   return [dir, file].join(pDelimeter);

}


async function fileSet({

   pData,
   pFile,
   pPath = getProjectPath(),
   pErrorMessage = 'Could not write to file.'

}) {

   try {

      await fs.writeFile(

         (pPath + pFile),
         {

            'txt' : () => {return pData},
            'json' : () => {return JSON.stringify(pData)}

         }[pFile.split('.').slice(-1)]()

      )

   } catch (error) {console.log(error); return pErrorMessage;}

}


async function fileGet({

   pFile,
   pEncoding = 'utf8',
   pPath = getProjectPath(),
   pErrorMessage = 'Could not read file.'

}) {

   try {

      const fin = await fs.readFile((pPath + pFile), pEncoding);
      return {

         'txt' : () => {return fin;},
         'json' : () => {return JSON.parse(fin);}

      }[pFile.split('.').slice(-1)]();
   
   } catch (error) {return pErrorMessage;}

}


async function fileDel({

   pFile,
   pPath = getProjectPath(),
   pErrorMessage = 'File does not exist.'

}) {

   try {await fs.unlink(pPath + pFile);}
   catch (error) {return pErrorMessage;}

}


// export <
module.exports = {

   fileSet,
   fileGet,
   fileDel

};

// >