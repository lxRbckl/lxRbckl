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


async function fileSet(

   pData,
   pFile,
   pPath = getProjectPath()

) {

   try {

      fs.writeFile(

         file = pPath + pFile,
         data = {

            'txt' : () => {return pData;},
            'json' : () => {return JSON.stringify(pData);}

         }[pFile.split('.').slice(-1)]()

      );

   } catch (error) {return 'Could not write to file.';}

}


async function fileGet(

   pFile,
   pEncoding = 'utf8',
   pPath = getProjectPath()

) {

   try {

      const fin = await fs.readFile(

         file = pPath + pFile,
         options = {encoding : pEncoding}

      );

      return {

         'txt' : () => {return fin;},
         'json' : () => {return JSON.parse(fin);}

      }[pFile.split('.').slice(-1)]();

   } catch (error) {return 'Could not read file.';}

}


(async () => {

   // set

   // get
   const file = 'sj.json';
   await fileSet(

      pData = {"test" : "test"},
      pFile = file

   );
   const fin = await fileGet(pFile = file);
   console.log(fin);

})();


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