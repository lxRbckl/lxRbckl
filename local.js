// import <
const fs = require('fs');
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


async function fileSet(

   pData,
   pFile,
   pPath = getProjectPath()

) {

   fs.writeFile(
      
      file = pPath + pFile, 
      data = {

         'txt' : () => {return pData;},
         'json' : () => {return JSON.stringify(pData);}

      }[pFile.split('.').slice(-1)](),
      (err) => {if (err) {return 'Could not write to file.';}}
   
   );
   
}


async function fileGet(

   pFile,
   pPath = getProjectPath()

) {

   fs.readFile(

      file = pPath + pFile,
      (error, data) => {

         console.log(error);
         console.log(data);

         if (error) {return 'Could not read file.';}
         else {

            return {

               'txt' : () => {return data;},
               'json' : () => {return JSON.parse(data);}

            }[pFile.split('.').slice(-1)]();

         }

      }

   )

}


console.log(fileGet(pFile = 'test.txt'));


async function fileDel(

   pFile,
   pPath = getProjectPath()

) {



}


// export <
module.exports = {

   fileSet,
   fileGet,
   fileDel

};

// >