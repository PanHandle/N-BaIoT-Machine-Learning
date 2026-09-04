for img in *.png; do
	convert "${img}" -resize 50% -quality 80 "${img%.png}_small.png"
done
