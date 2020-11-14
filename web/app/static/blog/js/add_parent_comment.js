function add_parent(id, author) {
    console.log(id);
    document.getElementById('contact_parent').value = id;
    document.getElementById('contact_comment').innerText = author + ', ';
}