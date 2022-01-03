Za početak klonirati ovaj repozitorij.
Zatim unutar ovog repozitorija klonirati https://github.com/ultralytics/yolov5.git
Sa google drivea preuzeti dataset i kopirati ga u repozitorij.

Direktorij exp36 kopirati u yolov5/runs/train


# Analiza podataka

Za analizu podataka pozicionirati se u mapu repozitorija i pokrenuti naredbu:

"tensorboard --logdir yolov5/runs/train"

Na localhostu:6006 će se pokazati svi grafovi vezani u treniranje.