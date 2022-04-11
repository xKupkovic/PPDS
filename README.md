# PPDS

## Co-programs

My program simulates running multiple generator instances.

Feeding __scheduler__ with different sizes set-ups generator for each size.
Those sizes represent max amount of yields that can be run in generator.
Each generator normally returns formatted string with id and current value which is then printed in scheduler.

When generator is called to yield next variable that is over limit it returns None.
None value is handled in scheduler as end condition and returns function