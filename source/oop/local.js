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


class local {

   constructor(

      pDelimeter = '/',
      pReferencePath = ''

   ) {

      this.delimeter = pDelimeter;
      this.referencePath = pReferencePath;

   }


   _getProjectPath() {

      const dir = path.dirname(__filename).split(/[/\\]/);
      const base = dir.includes('node_modules') ? -3 : -1;

      return dir.slice(0, base).join(this.delimeter);

   }


   async exists({

      pDir,
      pName,

      pPath = this._getProjectPath()

   }) {

      const dir = await this.getDir({pDir : pDir, pPath : pPath});
      const location = dir.indexOf(pName);

      return location != -1;

   }


   async setFile({

      pData,
      pFile,

      pPath = this._getProjectPath()

   }) {

      try {

         await writeFile(

            (pPath + this.referencePath + pFile),
            {

               'txt' : () => {return pData;},
               'json' : () => {return JSON.stringify(pData);}

            }[pFile.split('.').slice(-1)]()

         );

      } catch (error) {return 'Could not write to file.';}

   }


   async getFile({

      pFile,

      pEncoding = 'utf8',
      pPath = this._getProjectPath()

   }) {

      try {

         const fin = await readFile(

            (pPath + this.referencePath + pFile),
            pEncoding

         );

         return {

            'txt' : () => {return fin;},
            'json' : () => {return JSON.parse(fin);}

         }[pFile.split('.').slice(-1)]();

      } catch (error) {return 'Could not read file.';}

   }


   async delFile({

      pFile,

      pPath = this._getProjectPath()

   }) {

      try {await unlink(pPath + this.referencePath + pFile);}
      catch (error) {return 'File does not exist.';}

   }


   async setDir({

      pDir,

      pPath = this._getProjectPath()

   }) {

      try {await mkdir(pPath + this.referencePath + pDir);}
      catch (error) {return 'Could not create directory.';}

   }


   async getDir({

      pDir,

      pPath = this._getProjectPath()

   }) {

      try {return await readdir(pPath + this.referencePath + pDir);}
      catch (error) {return 'Directory does not exist.';}

   }


   async delDir({

      pDir,

      pPath = this._getProjectPath()

   }) {

      try {await rmdir(pPath + this.referencePath + pDir);}
      catch (error) {return 'Directory does not exist.';}

   }

}


// export <
module.exports = local;

// >