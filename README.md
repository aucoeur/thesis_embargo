## Caltech Library - Thesis Embargo
Utility to integrate and semi-automate workflow process for Caltech Library Thesis Embargo requests with gsuite/Google Workspace

## How to Use
1. Clone repo, then install dependencies: `npm install`

2. Login w/ clasp and authorize using your Google account via Terminal.
    > Note: Conflicts may occur if logged into Google and/or Chrome with multiple accounts
   ```
    npx clasp login
    ```
    - Turn on Google Apps Script API at https://script.google.com/home/usersettings

3. Create a new Google Script bound to a Google Sheet (or set the type as standalone to create a standalone script in your Google Drive)

    ```
    npx clasp create --type sheets --title "Caltech Library Thesis Embargo" --rootDir ./build
    ```

4. Include the necessary [OAuth Scopes](https://developers.google.com/oauthplayground/) in the [appsscript.json](./appsscript.json) file

5. Deploy the project     
    > The `build` directory contains the bundled code that is pushed to Google Apps Script.

    - Development mode: `npm run deploy`
        > On first run, review and approve permissions in Script Editor.  Because this is a private tool, there may be a warning that the app isn't verified. Show Advanced > Go 
    - Production mode:  `npm run deploy:prod`

    ### Development vs Production mode

    In production mode, the function names and variable names are shrinked and the output code is auto-minified. The production flag is not recommended for testing and debugging the Apps Script code.

    ### The .claspignore file

    The `.claspignore` file allows you to specify file and directories that you do not wish to not upload to your Google Apps Script project via `clasp push`.

    The default `.claspignore` file in the Apps Script Starter kit will push all the JS and HTML inside the `rootDir` folder and ignore all the other files.

### Optional
- Install a Trigger to open Sidebar on Open:
    1. In the Script Editor menu > Edit > Current project's triggers 
    1. + Add Trigger
        - Choose which function to run: `showSidebar`
        - Select event source: `From spreadsheet`
        - Select event type: `On open`
    1. Save

## Credits
 - Apps Script Starter Kit - [@labnol](https://github.com/labnol/apps-script-starter)
 - Materialize CSS - https://materializecss.com/

## Contributors
Aucoeur Ngo - [@aucoeur](https://github.com/aucoeur)   
Audi Blades - [@ablades](https://github.com/ablades)   
George Aoyagi - [@gaoyagi](https://github.com/gaoyagi)   
Jeric Hunter - [@JericHunter](https://github.com/JericHunter)   
Padyn Riddell - [@squeaky1273](https://github.com/squeaky1273)  
