---
title: "Ben Goddard - Research"
layout: textlay
excerpt: "Ben Goddard -- Research"
sitemap: false
permalink: /research/
---

# Research

## General Interests

<div class="col-sm-12 clearfix">

I am interested in the derivation and analysis of reduced models for complex physical systems. In particular, I use a synergistic approach combining modelling, mathematical analysis and numerics to study phenomena in a wide range of mathematical physics including [soft/condensed matter physics](#soft-matter), [quantum molecular dynamics](#quantum-molecular-dynamics), and the [electronic structure](#electronic-structure) of atoms and molecules.  I also have interests in [Mathematical Biology](#mathematical-biology) and [PDE-constrained optimisation](#pde-constrained-optimisation).

</div>


## Soft Matter

<div class="col-sm-12 clearfix">

Joint work with [Serafim Kalliadasis](http://www3.imperial.ac.uk/complexmultiphasesystems) (Imperial College London, Chem. Eng.),
[Andreas Nold](https://www.researchgate.net/profile/Andreas_Nold)
(Max Plank Institute for Brain Research),
[Raffaella Ocone](https://researchportal.hw.ac.uk/en/persons/raffaella-ocone) (Heriot-Watt University, Engineering),
[Greg Pavliotis](http://www2.imperial.ac.uk/~pavl/) (Imperial College London, Maths),
[Nikos Savva](http://www.cardiff.ac.uk/maths/contactsandpeople/profiles/savvan.html) (Cardiff University, Maths),
[David Sibley](http://www.lboro.ac.uk/departments/maths/staff/academic/david-sibley/)  (Loughborough University, Maths),
[Jin Sun](http://www.homepages.ed.ac.uk/jsun/) (University of Edinburgh, Engineering),
[Job Thijssen](https://www2.ph.ed.ac.uk/~jthijsse/) (University of Edinburgh, Physics),
[Mark Wilkinson](https://markwilkinson-hw.wixsite.com/homepage) (Nottingham Trent University, Mathematics),
and
[Petr Yatsyshin](http://www3.imperial.ac.uk/complexmultiphasesystems/group/yatsyshin) (Imperial College London, Chem. Eng.)

Soft matter is a broad (and, for a mathematician's point of view, poorly defined) term that describes materials that are easily deformed under the application of external forces, such as gravity or pressure,
at room temperature  Typical everyday examples include soaps, gels, foams, paints, gels, liquid crystals and biological matter.  The aim of this research is to understand and elucidate the fundamental physics behind the behaviour of such materials both in and our of equilibrium.

![]({{ site.url }}{{ site.baseurl }}/images/research/Colloids.png){: style="width: 400px; float: right; border: 10px"}

Such effects are highly multiscale since interactions on the microscopic, particle-size scale strongly affect the  macroscopic behaviour. Such problems require a careful combination of modelling, rigorous mathematical analysis and numerics.  Since the experimental observation of Brownian motion in the 19th century and the foundation of statistical mechanics by Einstein at the start of the 20th century, colloidal fluids (consisting of many microscopic particles suspended in a fluid bath) have been model systems for both experimental and theoretical scrutiny.  Typical examples of colloidal fluids are milk, blood and ink, and recent advances in biophysics and nanotechnology have stimulated great interest in the dynamics of such soft matter.

Due to the large numbers of particles, direct computation of the dynamics becomes intractable and reduced models are necessary. Ideally, we would like reduced equations with dimension independent of the number of particles. In recent years one such class of models, known as dynamical density functional theories (DDFTs), has received increasing attention. Existing DDFTs neglect either the inertia of the colloidal particles, or hydrodynamic interactions (bath-mediated forces), or both. However, these effects are crucial for understanding the dynamics of many colloidal systems and a more general DDFT is required.

We have rigorously derived a DDFT formalism including all crucial physical effects, which contains many existing DDFTs as special cases.  Via a rigorous homogenization argument, we have shown that the true DDFT in the high friction limit differs from that obtained by more heuristic arguments.  In particular, the rigorously-derived DDFT included a density-dependent diffusion tensor. We have also implemented an efficient numerical scheme based on the extension of spectral methods to integro-partial-differential equations to solve DDFTs. The scheme allows us to demonstrate the excellent agreement with the full underlying stochastic dynamics for a range of systems and to tackle a wide range of problems in soft matter.
 
Recently, we have been working to extend these methodologies to granular media (in which the bath has very low, or even zero, viscosity).  We have derived an associated DDFT which requires externally-determined parameters.  Through a combination of microscopic simulations and data-science approaches, we have determined appropriate values for these parameters and numerically implemented the associated DDFTs.  This has allowed us to elucidate the important physical effects in inelastic granular media.
</div>


## Quantum Molecular Dynamics

<div class="col-sm-12 clearfix">

Joint work with
[Volker Betz](http://www.mathematik.tu-darmstadt.de/~betz/) (TU Darmstadt, Maths),
[Adam Kirrander](http://www.kirrander.chem.ed.ac.uk/) (University of Edinburgh, Chemistry),
[Caroline Lasser](https://www.professoren.tum.de/en/lasser-caroline/) (TU Munich, Mathematics),
[Uwe Manthe](https://www.uni-bielefeld.de/chemie/tc/Manthe/) (Universit&auml;t Bielefeld, Chemistry),
and 
[Stefan Teufel](https://www.maphy.uni-tuebingen.de/members/stte) (Universit&auml;t T&uuml;bingen, Maths).

The aim of quantum molecular dynamics is to solve the time-dependent Schr&ouml;dinger equation, which describes the motion of the electrons and nuclei in atoms and molecules.  Since nuclei are much (at least a few thousand) times heavier than electrons, the timescales associated with the motion of nuclei and electrons are generally well-separated.  In particular, when electronic energy levels for a given molecule are well-separated, the nuclear and electronic dynamics decouple, leading to the Born-Oppenheimer approximation under which the electrons are assumed to equilibrate instantaneously from the point of view of the nuclei.  This dramatically reduces the complexity of the problem (however, it is still hard!).

![]({{ site.url }}{{ site.baseurl }}/images/research/Photodissociation.png){: style="width: 400px; float: left; border: 10px"}

Despite its success, situations in which the Born-Oppenheimer approximation fails are of great interest in quantum chemistry.  These occur when the electronic energy levels are not well-separated for a given nuclear configuration.  Important applications include the photodissociation of diatomic molecules like NaI (sodium iodide), or the reception of light in the retina. Two basic types of failure occur: conical (or full) crossings as appearing, and avoided crossings. The latter are typical for systems withone nuclear degree of freedom, and are the topic of much of our research.

The simplest example of such a system is a dimer (a molecule with two atoms, such as NaI) for which we consider only the interatomic separation.  This is a 1D problem and, for a particular separation, the lowest two energy levels become very close but do not cross.  In a typical experiment, a laser excites the electrons, which change configuration.  This in turn causes a force on the nuclei, causing them to move apart.  When the electronic energy levels are well-separated, the Born-Oppenheimer approximation is very accurate and only the dynamics on the excited energy level need to be considered.  However, near the avoided crossing, the energy levels couple and an exponentially small part of the wavepacket is transferred to the lower energy level.  This purely quantum effect is crucial in many ultrafast reactions.

To understand such processes, it is crucial to be able to predict the size and shape of the transmitted wavepacket.  The main difficulties are that it is both exponenetially small (meaning that numerical errors are likely to swamp the true result) and very quickly oscillating (meaning that a very fine grid is needed).  Hence such problems are numerically highly challenging.  Our work bypassed this issue via careful application of a mathematical technique called superadiabatic projections.  This allowed us to derive an explicit formula for the transmitted wavepacket.  This led to the determination of an efficient and accurate algorithm, the result of which agrees with highly-accurate numerical simulations for a wide range of wavepackets and potentials.  We have recently extended our results to arbitrary dimension (degrees of freedom), and demonstrated the excellent accuracy in 2D.

</div>

## Electronic Structure

<div class="col-sm-12 clearfix">

Joint work with [Gero Friesecke](http://www-m7.ma.tum.de/bin/view/Analysis/GeroFriesecke) (TU Munich, Mathematics).

The principal aim of quantum chemistry is to solve the (non-relativistic, Born-Oppenheimer) electronicSchr&ouml;dinger equation. To paraphrase Dirac, in principle, this allows the prediction of all chemical and physical properties of the system. However, due to the dimension scaling exponentially with the number of particles, standard numerical techniques are unsuitable, and an approximate model must be treated. In addition, this is a tough multi-scale problem; interest lies not in absolute energies, but in energy differences, which are generally several orders of magnitude smaller.

![]({{ site.url }}{{ site.baseurl }}/images/research/CSpectrum.png){: style="width: 400px; float: right; border: 10px"}

Although very successful, most numerical methods are based on chemical intuition and computationalexperience. In addition, the best calculated wavefunctions are linear combinations of millions or even billions of Slater determinants (N-particle basis functions). This presents major problems when trying to analyse such wavefunctions, and in interpreting them in terms of standard textbook chemistry models, such as orbital shell filling (the Aufbau principle).

We have shown that many of the interesting chemical properties of small atoms and ions can be demonstratedthrough the `PT model', based on first order perturbation theory. This model consists of fixing the number of electrons (which determine the chemistry) and increasing the nuclear charge.  Such sequences of ions are realised in nature, which allows us to compare directly to experiment. We find that, for moderately charged ions, our model produces highly accurate results. In addition, this approximation is exactly soluble, by hand! This is somewhat surprising as, for the case of Carbon, it requires diagonalizing a 70&times;70 matrix. The resulting simple wavefunctions can be written out explicitly and lead to increased insight into the fundamental physics and chemistry underlying the behaviour of atoms.

By suggesting a novel scaling in which to plot energies of isoelectronic sequences, our results led to theidentification of incorrectly assigned experimental results for five-electron ions. It alsoallows, through cubic spline fitting, to predict the values of missing experimental energy levels, and for some empirical chemical observations to be studied rigorously. For example, asymptotic ground states differ from those traditionally described in chemistry, by small but interesting corrections, which dramatically alter properties such as relative electron positions, providing insight into chemical bond angles.

Unfortunately, for neutral atoms the energies produced by this model are not chemically accurate.This is a result of its failure to satisfy the virial theorem, which enforces a ratio of the kinetic andpotential energies. We therefore extended the model by introducing three variational parameters (analogousto widely-used 'screening parameters'), producing the first mathematical definition of a ConfigurationInteraction model. This model is 'minimal' in the sense that it contains the smallest basis, withthe fewest parameters, such that it is symmetry preserving, asymptotically exact, and satisfies the virialtheorem. Up to minimization over the three parameters, it remains exactly soluble by hand. The energiesobtained for atoms are comparable to (and in some cases better than) those of much larger numerical models.

Our simple wavefunctions and a novel definition of bond angle in a trimer withtwo hydrogen atoms and a central atom X, allowed us to accurately predict, from first principles,the H-X-H bond angles.This angle depends on the bond length and, for a number of cases is not unique (a consequence of thenon-uniqueness of the ground state) and thus we predict a continuous range of possible bond angles, all withthe same energy of the central atom. Atoms with such bond angle ranges can be thought of as more 'flexible' and thus able to form a greater range of bonds (i.e. molecular geometries), with no energy penalty to the central atom. For sensible choices of the bond length, the predicted bond angles agree well with experiment for all first row atoms. In addition, we have shown that the small corrections to the standard Aufbau model are critical in predicting these bond angles.</div>
## Mathematical Biology

<div class="col-sm-12 clearfix">

Joint work with 
[David Tollervey](https://www.wcb.ed.ac.uk/research/tollervey) 
and [Tomasz Turowski](http://tollervey.bio.ed.ac.uk/) (University of Edinburgh, Wellcome Centre for  Cell Biology).

![]({{ site.url }}{{ site.baseurl }}/images/research/RNATranscription.png){: style="width: 400px; float: left; border: 10px"}

We are studying the effects of transcription elongation rates on RNA processing.  Generally, sequence-specific regulation is poorly understood.  We are using a combination of _in vivo_ experiments (done by my collaborators, so, thankfully, I don't need to go anywhere near a lab) and _in silico_ (i.e., computational) studies to elucidate some commonly-observed features of RNA transcription.  In particular, we focus on the uneven local polymerase occupancy (which suggests a substantial variation in transcription speed), and correlation of forward translocation with the folding energy.  Our mathematical model uses a stochastic jump process to model the interacting RNA polymerases as they transcribe along the RNA.  We find that the agreement between experiment and theory is very good, with almost all parameters in the model being determined experimentally (i.e., we haven't just [fitted an elephant](https://en.wikiquote.org/wiki/John_von_Neumann)). 

It is interesting to see that a relatively simple mathematical model (from my point of view, not necessarily a feeling shared by the biologists) can lead to very good agreement with experiment.  There are many interesting possible extensions to this work, which we hope to pursue in the near future.

</div>

## PDE-Constrained Optimisation

<div class="col-sm-12 clearfix">

Joint work with [James Maddison](https://www.maths.ed.ac.uk/~jmaddis2/) and
[John Pearson](https://sites.google.com/site/johnpearsonmaths/home) (University of Edinburgh, School of Mathematics).

![]({{ site.url }}{{ site.baseurl }}/images/research/PDECO.png){: style="width: 400px; float: right; border: 10px"}

One of the most common way of modelling large-scale physical systems is through the use of partial differential equations (PDEs); in particular, they can be used to model systems of interacting particles, such as molecules, cells, people, or stars.  There are many situations in which these systems can be controlled, for example though the use of external forces, or by the design of engineering devices.  Generally, there will be a desired target distribution of the particles, for example separating them based on size, or achieving rapid sedimentation under gravity.  A major challenge is to determine the optimal way in which to control these processes. Here, optimal reflects some balance between the distance of the solution from the target state and the cost, be it in terms of time, financial cost, or resources.  Mathematically, these problems are formulated in terms of PDE-constrained optimisation (PDECO).

Most mathematical work on PDECO has focussed on systems in which inter-particle interactions are neglected.  In some situations this is a reasonable assumption.  However, in many cases, the inter-particle interactions are one of the dominant effects in the system and qualitatively and quantitatively affect the dynamics.  For example, the attraction of yeast cells causes them to clump together (or flocculate), which significantly affects the sedimentation dynamics in the brewing process.

We are working to combine models from DDFT (which provide accurate solutions to the dynamics of interacting particles) with techniques from PDECO in order to tackle real-world, industrially-relevant applications.

</div>