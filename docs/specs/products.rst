.. doctest docs/specs/products.rst
.. _specs.products:

===================================================
``products`` : defining the things you sell and buy
===================================================

.. currentmodule:: lino_xl.lib.products

The :mod:`lino_xl.lib.products` plugin adds functionality for managing
"products".

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_pronto.projects.yvonne.settings.doctests')
>>> from lino.api.doctest import *



Products
========


.. class:: Products

    >>> rt.show(products.Products)
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    ==== ============== ================== ================== =========== =============
     ID   Designation    Designation (de)   Designation (fr)   Category    Sales price
    ---- -------------- ------------------ ------------------ ----------- -------------
     4    Metal chair    Stuhl aus Metall   Chaise en métal    Furniture   79,99
     3    Metal table    Tisch aus Metall   Table en métal     Furniture   129,99
     2    Wooden chair   Stuhl aus Holz     Chaise en bois     Furniture   99,99
     1    Wooden table   Tisch aus Holz     Table en bois      Furniture   199,99
                                                                           **509,96**
    ==== ============== ================== ================== =========== =============
    <BLANKLINE>

.. class:: Services

    >>> rt.show(products.Services)
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    ================================================================ ================================================================ ================================================================ ===============
     Designation                                                      Designation (de)                                                 Designation (fr)                                                 Sales account
    ---------------------------------------------------------------- ---------------------------------------------------------------- ---------------------------------------------------------------- ---------------
     IT consultation & maintenance                                    EDV Konsultierung & Unterhaltsarbeiten                           ICT Consultation & maintenance
     Image processing and website content maintenance                 Bildbearbeitung und Unterhalt Website                            Traitement d'images et maintenance site existant
     Programming                                                      Programmierung                                                   Programmation
     Server software installation, configuration and administration   Server software installation, configuration and administration   Server software installation, configuration and administration
     Website hosting 1MB/month                                        Website-Hosting 1MB/Monat                                        Hébergement 1MB/mois
    ================================================================ ================================================================ ================================================================ ===============


.. class:: Category

    Can be used to group products into "categories".  Categories can be edited by the user.

    >>> rt.show(products.Categories)
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
    ==== ======== ================= ================== =============================== ==============
     ID   Parent   Designation       Designation (de)   Designation (fr)                Product type
    ---- -------- ----------------- ------------------ ------------------------------- --------------
     1             Furniture         Möbel              Meubles                         Products
     2             Website Hosting   Website-Hosting    Hébergement de sites Internet   Services
    ==== ======== ================= ================== =============================== ==============
    <BLANKLINE>


.. class:: ProductTypes

    Can be used to group products into "types".  Types cannot be edited by the
    user.  But every product type can have a layout on its own.

    >>> rt.show(products.ProductTypes)
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
    ======= ========== ========== ===================
     value   name       text       Table name
    ------- ---------- ---------- -------------------
     100     default    Products   products.Products
     200     services   Services   products.Services
     300     parts      Parts      products.Parts
    ======= ========== ========== ===================
    <BLANKLINE>


.. class:: DeliveryUnits

    The list of possible delivery units of a product.

    >>> rt.show(products.DeliveryUnits)
    ======= ======= =======
     value   name    text
    ------- ------- -------
     10      hour    Hour
     20      piece   Piece
     30      kg      Kg
    ======= ======= =======
    <BLANKLINE>
