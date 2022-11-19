

// Displaying Chapters
window.onload = () => {
    const body = document.getElementById('chapters');
    for (const chapter in chapterList) {

        var chapData = chapterList[chapter];

        // Creating tags
        var chapterDom = document.createElement('div');
        var aTag = document.createElement('a');

        // Adding Attributes
        var chapterLink = `/chapters/${chapData['chapter-id']}`;
        aTag.setAttribute('href', chapterLink);
        aTag.setAttribute('onclick', 'showBar()');        
        aTag.style = "cursor: pointer;";
        aTag.innerText = chapData['chapter-title'];
        chapterDom.className = 'chapter';

        // Appending in DOM
        chapterDom.appendChild(aTag);
        body.appendChild(chapterDom);

    }
}

// listener event for a tag
var showBar = () => {
    topbar.show();
    return true;
}