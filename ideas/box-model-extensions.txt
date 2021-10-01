====== Extensions de modèle de boîte ======
Nous voulons définir plusieurs nouvelles choses qui iraient correctement dans Box Model, mais nous ne voulons pas attendre que le module le plus compliqué de CSS soit terminé (ou même correctement démarré). Nous devrions donc créer un nouveau module qui ajoute quelques "extensions" au modèle de boîte, en supposant que le scénario de base sera correctement défini ultérieurement.

===== Rapport d'aspect =====
Tel que défini à l'adresse http://www.xanthir.com/blog/b4810.

Accorderait la possibilité de spécifier un "rapport d'aspect" pour une boîte, verrouillant sa largeur et sa hauteur dans un rapport défini. Cela peut actuellement être partiellement piraté en exploitant quelques détails mineurs sur le fonctionnement des pourcentages dans le remplissage, mais cela doit être explicite, ce qui est préférable et permet un traitement plus approfondi.

<note>
This has been adopted into [[https://www.w3.org/TR/css-sizing-4/|CSS Box Sizing Level 4]].
</note>

===== Taille Mots-clés =====
Le mot clé '' auto '' pour largeur et hauteur donne des valeurs intéressantes en fonction du contexte, qui ne peuvent pas être dupliquées ailleurs. Par exemple, les tables et les flottants résolvent '' auto '' à l'aide de l'algorithme "shrinkwrap", tandis que les blocs normaux utilisent un algorithme "de remplissage" pour remplir leur parent autant que possible.

Ces comportements doivent être explicitement nommés pour pouvoir être utilisés de manière générale:
  * '' fill '': La largeur normale d'un élément display: block, où il remplit son parent.
  * '' min-content '': La largeur d'une boîte si vous prenez toutes les opportunités de saut de ligne facultatives.
  * '' max-content '': La largeur d'une boîte si vous ne prenez aucune opportunité de saut de ligne facultatif.
  * '' fit-content '': '' min (max-content, fill) ''

<note>
This has been adopted into [[https://www.w3.org/TR/css-sizing-3/|CSS Box Sizing Level 3]].
</note>