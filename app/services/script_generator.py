def generate_tiktok_variants(title: str, body: str, region: str):
    kurznews_script = f"{title}. {body[:120]}"

    warum_wichtig_script = (
        f"Diese Nachricht ist für junge Menschen in {region} relevant, "
        f"weil sie direkten Einfluss auf Alltag, Mobilität oder wirtschaftliche Entwicklung haben kann. "
        f"{body[:100]}"
    )

    drei_fakten_script = (
        "Drei Dinge, die du wissen musst: "
        f"Erstens: {title}. "
        "Zweitens: Es geht um konkrete Veränderungen in der Region. "
        "Drittens: Die Folgen könnten viele Menschen direkt betreffen."
    )

    return [
        {
            "angle": "kurznews",
            "hook": "Neue Nachricht aus Sachsen",
            "script": kurznews_script,
            "caption": "News aus Ostdeutschland",
            "hashtags": ["#news", "#ostdeutschland"]
        },
        {
            "angle": "warum_wichtig",
            "hook": "Warum diese Nachricht wichtig ist",
            "script": warum_wichtig_script,
            "caption": "Warum das relevant ist",
            "hashtags": ["#politik", "#news"]
        },
        {
            "angle": "3_fakten",
            "hook": "3 Dinge die du wissen musst",
            "script": drei_fakten_script,
            "caption": "Kurz erklärt",
            "hashtags": ["#erklärung", "#news"]
        }
    ]