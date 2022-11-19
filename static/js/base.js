// For search Box
function searchQuery(e) {
    topbar.show();
    var query
    query = document.querySelector('#search-box input').value;
    window.location.href = `/?search=${query}`;
}

// For enter in search box
document.getElementById(
    "search-box"
).addEventListener(
    'keypress',
    (e) => {
        if (e.key == "Enter") {
            searchQuery(e);
        };
    }
);

const showTopbar = (url) => {
    topbar.show();
    //redirecting to url
    window.location.href = url;
}

// On clicking on search icon
document.getElementById(
    "search-btn"
).addEventListener(
    'click',
    (e) => {
        searchQuery(e);
    }
);

//check if any links are clicked then show topbar
document.querySelectorAll('a').forEach(
    (a) => {
        a.addEventListener(
            'click',
            (e) => {
                topbar.show();
            }
        )
    }
)
