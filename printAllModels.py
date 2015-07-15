from www.models import Match, Country, Player

list(Player.objects.all())
list(Country.objects.all())
list(Match.objects.all())


c = Country.objects.get(country="Chile"
p = Player.objects.get(player="Claudio Bravo")
c.captain
c.captain = p
