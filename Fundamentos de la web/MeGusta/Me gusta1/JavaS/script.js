function addlike(buttonElement) {
let parentDiv = buttonElement.parentNode;
let AddLikes = parentDiv.querySelector('.numLikes');
let numLikes = parseInt(AddLikes.textContent) + 1;
AddLikes.textContent = numLikes.toString();
}