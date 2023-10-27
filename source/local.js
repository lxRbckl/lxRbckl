// import <
const path = require('path');
const {

   mkdir,
   rmdir,
   unlink,
   readdir,
   readFile,
   writeFile

} = require('fs/promises');

// >


function getProjectPath(
   
   pFile = '',
   pDelimeter = '/'
   
) {

   const file = pFile.split(/[/\\]/);
   const dir = path.dirname(__filename).split(/[/\\]/);

   return [...dir.slice(0, -1), ...file].join(pDelimeter);

}


async function fileSet({

   pData,
   pFile,
   pPath = getProjectPath(),
   pErrorMessage = 'Could not write to file.'

}) {

   try {

      await writeFile(

         (pPath + pFile),
         {

            'txt' : () => {return pData},
            'json' : () => {return JSON.stringify(pData)}

         }[pFile.split('.').slice(-1)]()

      )

   } catch (error) {return pErrorMessage;}

}


async function fileGet({

   pFile,
   pEncoding = 'utf8',
   pPath = getProjectPath(),
   pErrorMessage = 'Could not read file.'

}) {

   try {

      const fin = await readFile((pPath + pFile), pEncoding);
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

   try {await unlink(pPath + pFile);}
   catch (error) {return pErrorMessage;}

}


async function dirSet({

   pDir,
   pPath = getProjectPath(),
   pErrorMessage = 'Could not create directory.'

}) {

   try {await mkdir(pPath + pDir)}
   catch (error) {console.log(error); return pErrorMessage;}

}


async function dirGet({

   pDir,
   pPath = getProjectPath(),
   pErrorMessage = 'Directory does not exist.'

}) {

   try {return await readdir(pPath + pDir);}
   catch (error) {return pErrorMessage;}

}


async function dirDel({

   pDir,
   pPath = getProjectPath(),
   pErrorMessage = 'Directory does not exist.'

}) {

   try {await rmdir(pPath + pDir);}
   catch (error) {return pErrorMessage;}

}


// export <
module.exports = {

   fileSet,
   fileGet,
   fileDel,
   dirSet,
   dirGet,
   dirDel

};

// >