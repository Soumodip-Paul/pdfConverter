
let isAdvancedUpload = () => {
    var div = document.createElement('div');
    return (('draggable' in div) || ('ondragstart' in div && 'ondrop' in div)) && 'FormData' in window && 'FileReader' in window;
};

let draggableFileArea = document.querySelector("#draggable_area");
let browseFileText = document.querySelector("#title_box");
let uploadIcon = document.querySelector("#icon_action");
let dragDropText = document.querySelector("#drop_files");
let fileInput = document.querySelector("#id_file_field");
let cannotUploadMessage = document.querySelector(".cannot-upload-message");
let cancelAlertButton = document.querySelector(".cancel-alert-button");
let uploadedFile = document.querySelector(".file-block");
let fileName = document.querySelector(".file-name");
let fileSize = document.querySelector(".file-size");
let progressBar = document.querySelector(".progress-bar");
let removeFileButton = document.querySelector(".remove-file-icon");
let uploadButton = document.querySelector("input[type='submit']");
let fileFlag = 0;

fileInput.addEventListener("click", () => {
    fileInput.value = '';
    browseFileText.innerHTML = '';
    uploadIcon.innerHTML = 'upload'
});

fileInput.addEventListener("change", e => {
    uploadIcon.innerHTML = 'check_circle';
    browseFileText.innerHTML = 'File Selected Successfully!';
});
/* 
 uploadButton.addEventListener("click", () => {
     let isFileUploaded = fileInput.value;
     if(isFileUploaded != '') {
         if (fileFlag == 0) {
             fileFlag = 1;
             var width = 0;
             var id = setInterval(frame, 50);
             function frame() {
                   if (width >= 390) {
                     clearInterval(id);
                     uploadButton.innerHTML = `<span class="material-icons-outlined upload-button-icon"> check_circle </span> Uploaded`;
                   } else {
                     width += 5;
                     progressBar.style.width = width + "px";
                   }
             }
           }
     } else {
         cannotUploadMessage.style.cssText = "display: flex; animation: fadeIn linear 1.5s;";
     }
 });
 
 cancelAlertButton.addEventListener("click", () => {
     cannotUploadMessage.style.cssText = "display: none;";
 });
 */
if (isAdvancedUpload) {
    ["drag", "dragstart", "dragend", "dragover", "dragenter", "dragleave", "drop"].forEach(evt =>{
        draggableFileArea.addEventListener(evt, e => {
            e.preventDefault();
            e.stopPropagation();
            if (evt === "dragleave")
                draggableFileArea.classList.remove('bg-gray-200')
            else
                draggableFileArea.classList.add('bg-gray-200')
            uploadIcon.innerHTML = 'upload';
            dragDropText.innerHTML = 'or drag and drop';
        })

        document.body.addEventListener(evt, e =>{
            e.preventDefault();
            e.stopPropagation();
        })
        }
    );

    ["dragover", "dragenter"].forEach(evt => {
        draggableFileArea.addEventListener(evt, e => {
            e.preventDefault();
            e.stopPropagation();
            uploadIcon.innerHTML = 'download';
            dragDropText.innerHTML = 'or drop your file here!';
        });
        document.body.addEventListener(evt, e =>{
            e.preventDefault();
            e.stopPropagation();
        })
    });

    draggableFileArea.addEventListener("drop", e => {
        let list = new DataTransfer();
        console.log(fileInput.accept)
        let files = Array.from(e.dataTransfer.files).filter(e => e.type === fileInput.accept);
        console.log(files)
        if (files.length === 0) return
        // files.forEach(e => list.items.add(e))
        list.items.add(files[0])

        fileInput.files = list.files;
        uploadIcon.innerHTML = 'check_circle';
        browseFileText.innerHTML = 'File Dropped Successfully!';
        uploadButton.innerHTML = `Upload`;
        draggableFileArea.classList.remove('bg-gray-200')
    });
    document.body.addEventListener("drop", e =>{
        e.preventDefault();
        e.stopPropagation();
    })
}
  /*
removeFileButton.addEventListener("click", () => {
    uploadedFile.style.cssText = "display: none;";
    fileInput.value = '';
    uploadIcon.innerHTML = 'file_upload';
    dragDropText.innerHTML = 'Drag & drop any file here';
    document.querySelector(".label").innerHTML = `<span class="browse-files"> <input type="file" class="default-file-input"/> <span class="browse-files-text">browse file</span> <span>from device</span> </span>`;
    uploadButton.innerHTML = `Upload`;
});
*/