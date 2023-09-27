let currentGameName = '';
let correctAnswersCount = 0;
const MAX_TRIES = 3;

function fetchGameData(gameName) {
    currentGameName = gameName;
    fetch('/api/' + gameName)
    .then(response => response.json())
    .then(data => {
        document.getElementById('rules').innerText = data.rules;
        document.getElementById('question').innerText = data.question;
        document.getElementById('answer').innerText = data.answer;

        document.getElementById('rules').style.display = 'block';
        document.getElementById('apiResultModal').style.display = 'block';
        document.getElementById('question').style.display = 'block';
        document.getElementById('answer').style.display = 'none';
        document.getElementById('tryAgain').style.display = 'none';
        document.getElementById('submitBtn').style.display = 'block';
        document.getElementById('userAnswer').style.display = 'block';
        document.getElementById('userAnswer').value = '';
    });
}

function fetchNextGameData(gameName) {
    fetchGameData(gameName);
}

function restartGame() {
    correctAnswersCount = 0;
    fetchGameData(currentGameName);
    document.getElementById('rules').style.display = 'block';
    document.getElementById('question').style.display = 'block';
    document.getElementById('answer').style.display = 'none';
    document.getElementById('tryAgain').style.display = 'none';
    document.getElementById('submitBtn').style.display = 'block';
    document.getElementById('userAnswer').style.display = 'block';
    document.getElementById('userAnswer').value = '';
}

function checkAnswer() {
    const userAnswer = document.getElementById('userAnswer').value;
    const correctAnswer = document.getElementById('answer').innerText;

    console.log("User Answer:", userAnswer);

    if (userAnswer === correctAnswer) {
        correctAnswersCount++;
        if (correctAnswersCount === 3) {
            document.getElementById('answer').style.display = 'block';
            document.getElementById('rules').style.display = 'none';
            document.getElementById('answer').innerText = 'Congratulations! You won!';
            document.getElementById('question').style.display = 'none';
            document.getElementById('submitBtn').style.display = 'none';
            document.getElementById('userAnswer').value = '';
            document.getElementById('userAnswer').style.display = 'none';
            document.getElementById('tryAgain').style.display = 'block';
            correctAnswersCount = 0;
        } else {
            fetchGameData(currentGameName);
            document.getElementById('userAnswer').value = '';
        }
    } else {
        document.getElementById('answer').style.display = 'block';
        document.getElementById('answer').innerText = `${userAnswer} is wrong answer! The correct answer was ${correctAnswer}.`;
        document.getElementById('submitBtn').style.display = 'none';
        document.getElementById('tryAgain').style.display = 'block';
        document.getElementById('userAnswer').style.display = 'none';
        document.getElementById('userAnswer').value = '';
        correctAnswersCount = 0;
    }
}

function closeModal() {
    document.getElementById('apiResultModal').style.display = 'none';
}