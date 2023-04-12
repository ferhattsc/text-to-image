from big_sleep import Imagine

def  generate_image(text):

    dream = Imagine(
        text = text,
        lr = 5e-2,
        save_every = 100,
        text_min = "blur|zoom",
        save_date_time = True,
        max_classes=15,
        save_best=True,
        save_progress = True
    )

    return dream()

