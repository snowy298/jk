const signInButton = document.getElementById('signInButton');
const cooldownMessage = document.getElementById('cooldownMessage');
let cooldown = false;
const cooldownTime = 30 * 1000; // 30 seconds cooldown
let cooldownTimer;

signInButton.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent form submission for demonstration

    if (cooldown) {
        return;
    }

    // Simulate a sign-in process
    console.log('Sign In attempt...');
    startCooldown();
});

function startCooldown() {
    cooldown = true;
    signInButton.disabled = true;
    cooldownMessage.classList.remove('hidden');
    
    // Start cooldown timer
    cooldownTimer = setTimeout(() => {
        cooldown = false;
        signInButton.disabled = false;
        cooldownMessage.classList.add('hidden');
    }, cooldownTime);
}
