function turnOn() {
            document.querySelectorAll('.fan-img').forEach(img => {
                img.classList.add('rotating');
            });
            document.querySelectorAll('.fan-image-wrapper').forEach(div => {
                div.classList.remove('off-state');
                div.classList.add('on-state');
            });
        }

        function turnOff() {
            document.querySelectorAll('.fan-img').forEach(img => {
                img.classList.remove('rotating');
            });
            document.querySelectorAll('.fan-image-wrapper').forEach(div => {
                div.classList.remove('on-state');
                div.classList.add('off-state');
            });
        }