# Body Shape Analyzer

At the age of 17, I found that most magazines described women's body types  based on proportions. However, what someone may call 'wide hips' may not be wide enough to another person and this can lead to a lot of confusion. Here is how I  provide a more concrete method of analyzing women's body types.

![alt text](http://vinslookbook.com/wp-content/uploads/2015/08/girl-1535859_1920-683x1024.jpg)

<!-- wp:heading {"level":3} -->
<h3>Principle</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Women's body types are broadly classified as 7 types. They are:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Rectangle - Similar measurements for all sections of  the body.</li><li>Triangle - Large hips and a small bust.</li><li>Inverted Triangle - Broad shoulders and small hips.</li><li>Spoon - Large hips than shoulders.</li><li>Hourglass -  Hips proportionate to shoulders. Small waist.</li><li>Top Hourglass - buttocks larger than hips.</li><li>Bottom Hourglass - Bust proportionate to waist.</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3>Ideology</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Using measurements of a person's body, determine the proportions of the person's body to determine their body type. The measurements to be taken as parameters are: </p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Bust</li><li>Waist</li><li>Hips</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Device a formula for easy detection of each body type. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I came up with very crude formulas back then, in 2007. Now I decided to update the idea, by searching for more resources. Surprisingly, research has already been conducted to determine women's body types using formulas. I have incorporated them in my code.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Improved Method</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Lee JY, Istook CL, Nam YJ wrote a paper in which they proposed the following formulas for each body type:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Hourglass </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(bust − hips) ≤ 1" AND (hips − bust) &lt; 3.6" AND (bust − waist) ≥ 9" OR (hips − waist) ≥ 10"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Bottom hourglass </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(hips − bust) ≥ 3.6" AND (hips − bust) &lt; 10" AND (hips − waist) ≥ 9" AND (high hip/waist) &lt; 1.193</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Top hourglass </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(bust − hips) &gt; 1" AND (bust − hips) &lt; 10" AND (bust − waist) ≥ 9"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Spoon </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(hips − bust) &gt; 2" AND (hips − waist) ≥ 7" AND (high hip/waist) ≥ 1.193</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Triangle </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(hips − bust) ≥ 3.6" AND (hips − waist) &lt; 9"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Inverted Triangle </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(bust − hips) ≥ 3.6" AND (bust − waist) &lt; 9"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Rectangle </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(hips − bust) &lt; 3.6" AND (bust − hips) &lt; 3.6" AND (bust − waist) &lt; 9" AND (hips − waist) &lt; 10"</p>
<!-- /wp:paragraph -->

The body shape analyzer that I created is one of the components of my prototype app, now available on google play:

[<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSojpFFWqTqH_wHsjAwe--ZdKXrsSNZBDWNNz4qK8fYRX_wK0Wb&usqp=CAU">](https://play.google.com/store/apps/details?id=com.vins.vinslookbook&hl=en)

