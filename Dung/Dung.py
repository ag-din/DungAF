#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

"""
#####################################################
### ABSTRACT ARGUMENTATION FRAMEWORK - DUNG
#####################################################

### DUNG PACKAGE V.1.0 (2020)

### Lic. Agustina Dinamarca (agustinadinamarca@gmail.com)


                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
 
""" 

def is_attacked(arg, attacks):
	"""
	Given an AF it returns True if there is at least one argument in AF
	that attacks "arg", otherwise it returns False.

	Parameters
	----------
	arg (str or int): An argument
	attacks (list of 2-uples): Attack relations

	Returns
	-------
	Bool: True if "arg" is attacked, otherwise it returns False.

	"""
	for x in attacks:
		if x[1] == arg:
			return True
	return False


def get_arg_attackers(arg, attacks):
	"""
	Given an argument "arg" and the attack relations "attacks" return a set
	of arguments that attacks "arg".

	Parameters
	----------
	arg (str or int): An argument
	attacks (list of 2-uples): Attack relations

	Returns
	-------
	Set: Set of arguments that attacks "arg".

	"""
	attackers = set()
	for i in attacks:
		if i[1] == arg:
			attackers.add(i[0])
	return attackers


def get_attacked_args(set_of_args, attacks):
	"""
	Given a set of arguments "set_of_args" and the attack relations "attacks"
	return the set of arguments that "set_of_args" attacks.

	Parameters
	----------
	set_of_args (set): Set of arguments
	attacks (list of 2-uples): Attack relations

	Returns
	-------
	Set: Set of arguments that "set_of_args" attacks.

	"""
	attacked = set()
	for i in attacks:
		if i[0] in set_of_args:
			attacked.add(i[1])
	return attacked


def powerset(iterable):
	"""
	Powerset.

	Parameters
	----------
	iterable (list or set): Set of arguments

	Returns
	-------
	Set: Subsets of arguments

	"""
	s = list(iterable)
	return set(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1)))


def compute_acceptability(arg, E, relations):
	"""
	Return if the argument "arg" is acceptable or not respect the set of 
	arguments "E".
	
	An argument "arg" in AF is ACCEPTABLE with respect to "E"
	(subset de AF) if and only if "E" defends "arg", that is, forall "b" in AF
	such that (b,arg) in R, exists c in E such that (c,b) in R.

	Parameters
	----------
	arg (str or int): An argument
	E (set): A set of arguments
	relations (list of 2-uples): Attack relations

	Returns
	-------
	Bool: if the argument "arg" is acceptable or not respect the set of 
	arguments "E".

	"""
	attackers = get_arg_attackers(arg, relations)
	if attackers != None:
		atks = []
		for y in attackers:
			yStatus = False
			yAtackers = get_arg_attackers(y, relations)
			if len(yAtackers.intersection(E)) > 0:
				yStatus = True
			atks.append(yStatus)
		if all(atks):
			return True
		else:
			return False


def checkArgumentsInRelations(arguments, relations):
	"""
	Check if arguments in relations exist in arguments

	Parameters
	----------
	arguments (set) : Set of arguments
	relations (list of 2-uples): Attack relations

	Returns
	-------
	Bool: True if all arguments in relations exist in arguments, else False

	"""
	if len(arguments) > 0:
		if len(relations) > 0:
			for x in relations:
				lst = []
				status = True
				if x[0] not in arguments or x[1] not in arguments:
					status = False
				lst.append(status)	 
				if all(lst):
					return True
				else:
					return False
		else:
			return True
	else:
		return False


class Extensions:
	"""
    Class used to represent extensions

    ...

    Attributes
    ----------
    arguments (set): Set of arguments
    extensions (set): Attack relations

    Methods
    -------
    get_Extensions()
        Return extensions
	get_SkepticallyAcceptedArguments()
		Return skeptiacally accepted arguments
	get_CredulouslyAcceptedArguments()
		Return credulously accepted arguments
	get_RejectedArguments()
		Return rejected arguments
    """
	def __init__(self, extensions, arguments):
		self.__extensions = extensions
		self.__arguments = arguments

	def get_Extensions(self):
		"""
		Return extensions

		Parameters
		----------
		None

		Returns
		-------
		Set: Extensions

		"""
		return self.__extensions
		
	def get_SkepticallyAcceptedArguments(self):
		"""
		Return set of skeptically accepted arguments

		Parameters
		----------
		None

		Returns
		-------
		Set: Skeptically accepted arguments

		"""
		accepted = set()
		if len(self.__extensions) > 0:
			for a in self.__arguments:
				lst = []
				for extension in self.__extensions:
					if a in extension:
						lst.append(True)
					else:
						lst.append(False)
				if all(lst):
					accepted.add(a)
		return accepted

	def get_CredulouslyAcceptedArguments(self):
		"""
		Return set of credulously accepted arguments

		Parameters
		----------
		None

		Returns
		-------
		Set: Credulously accepted arguments

		"""
		accepted = set()
		if len(self.__extensions) > 0:
			for a in self.__arguments:
				for extension in self.__extensions:
					if a in extension:
						accepted.add(a)
		return accepted

				
	def get_RejectedArguments(self):
		"""
		Return set of rejected arguments

		Parameters
		----------
		None

		Returns
		-------
		Set: Rejected arguments

		"""
		rejected = set()
		if len(self.__extensions) > 0:
			for a in self.__arguments:
				lst = []
				for extension in self.__extensions:
					if a in extension:
						lst.append(False)
					else:
						lst.append(True)
					if all(lst):
						rejected.add(a)
		return rejected

class Dung:
	"""
    Class used to represent a Dung Argumentation Framework

    ...

    Attributes
    ----------
    arguments (set): Set of arguments
    relations (set): Attack relations
    semantics (Class Semantics): Acceptability semantics

    Methods
    -------
    compute_cfs()
        Compute conflic-free subsets of arguments
	compute_admissibility()
		Compute abmissible set of arguments
    """
	def __init__(self, arguments, relations):
		self.__arguments = arguments
		self.__relations = relations
		self.semantics = Dung.Semantics(self)

	def compute_cfs(self):
		"""
		Return conflic-free subsets

		Parameters
		----------
		None

		Returns
		-------
		Set: Conflict-free subsets

		"""
		pwr = powerset(self.__arguments)
		if len(self.__arguments) > 0:
			if len(self.__relations) > 0:
				for x in self.__relations:
					x1 = x[0]
					x2 = x[1]
					dele = []
					for i in pwr:
						if (x1 in i) and (x2 in i):
							dele.append(i)
					for e in dele:
						pwr.remove(e)
		return set(pwr)


	def compute_admissibility(self):
		"""
		For each conflict free subset, if its attackers are
		attacked (exhaustively) by a subset of that cfs, it is admissible
		A conglict-free set of arguments S is ADMISIBLE iff each argument
		in S is ACCEPTABLE with respect to S.

		Parameters
		----------
		None

		Returns
		-------
		Set: Admissible arguments subsets

		"""
		cfs = self.compute_cfs()
		admissible = []
		if checkArgumentsInRelations(self.__arguments, self.__relations) == True:
			if len(cfs) > 0:
				for cfset in cfs:
					if len(cfset) >= 0:
						attackers = set()
						for cfsetmember in cfset:
							attackers = attackers.union(get_arg_attackers(cfsetmember, self.__relations))
						attackedbycfsmembers = []
						for attacker in attackers:
							atk = False
							attackedby = get_arg_attackers(attacker, self.__relations)
							for cfsetmember in cfset:
								if cfsetmember in attackedby:
									atk = True
							attackedbycfsmembers.append(atk)
						if all(attackedbycfsmembers):
							if cfset == ():
								admissible.append(set())
							else:
								d = set()
								for k in cfset:
									for kk in k:
										d.add(kk)
								admissible.append(d)
				return admissible
			else:
				return []
		else:
			return None

	
	class Semantics:
		def __init__(self, af):
			self.af = af

		def compute_stable_extensions(self):
			"""
			E is a stable extension of AF only if it is a conflict-free set that attacks 
			every argument that does not belong in E (formally, forall a in A\E, exists 
			b in E forall a in A\E,exists b in E such that (b,a) in R(b,a) in R.

			Parameters
			----------
			None

			Returns
			-------
			Set: Stable extensions subsets

			"""
			if checkArgumentsInRelations(self.af._Dung__arguments, self.af._Dung__relations) == True:
				adm = self.af.compute_cfs()
				stb = []
				if len(adm) > 0:
					for x in adm:
						if set(x).union(get_attacked_args(set(x), self.af._Dung__relations)) == self.af._Dung__arguments:
							stb.append(x)
				ext = Extensions(stb, self.af._Dung__arguments)
				return ext
			else:
				return None

		
		def compute_grounded_extensions(self):
			"""
			E is the (unique) grounded extension of AF only if it is the smallest element 
			(with respect to set inclusion) among the complete extensions of S.

			Parameters
			----------
			None

			Returns
			-------
			Set: Grounded extensions subsets

			"""
			if checkArgumentsInRelations(self.af._Dung__arguments, self.af._Dung__relations) == True:
				grd = []
				compExt = self.af.semantics.compute_complete_extensions()
				count = 0
				l = -99
				ce = compExt.get_Extensions()
				if len(ce)>0:
					for conj in ce:
						if count == 0:
							l = len(conj)
						else:
							if len(conj) < l:
								l = len(conj)
						count+=1
					
					for x in ce:
						if len(x) == l:
							grd.append(x)

				ext = Extensions(grd, self.af._Dung__arguments)
				
				return ext
			else:
				return None

		
		def compute_preferred_extensions(self):
			"""
			E is a preferred extension of AF only if it is a maximal element
			(with respect to the set-theoretical inclusion) among the admissible sets
			with respect to AF.

			Parameters
			----------
			None

			Returns
			-------
			Set: Preferred extensions subsets

			"""
			if checkArgumentsInRelations(self.af._Dung__arguments, self.af._Dung__relations) == True:
				pref = []
				adm = self.af.compute_admissibility()
				if len(adm) > 0:
					maxLen = 0
					## busco el conjunto admisible más grande
					for i in adm:
						if len(i) > maxLen:
							maxLen = len(i)
						## busco el conjunto admisible con número de elementos == maxLen
					for i in adm:
						if len(i) == maxLen:
							pref.append(i)

				ext = Extensions(pref, self.af._Dung__arguments)
				return ext
			else:
				return None

		
		def compute_complete_extensions(self):
			"""
			An admissible set S of arguments is called a complete extension iff
			each argument, which is acceptable with respect to S, belongs to S.

			Parameters
			----------
			None

			Returns
			-------
			Set: complete extensions subsets

			"""
			if checkArgumentsInRelations(self.af._Dung__arguments, self.af._Dung__relations)==True:
				compl = []
				adm = self.af.compute_admissibility()
				if len(adm) > 0:
					for conj in adm:
						accArgs = set()
						for x in self.af._Dung__arguments:
							if compute_acceptability(x, conj, self.af._Dung__relations) == True:
								accArgs.add(x)
						if accArgs == conj:
							compl.append(conj)

				ext = Extensions(compl, self.af._Dung__arguments) 
				return ext
			else:
				return None

