# encoding: utf-8

from __future__ import print_function
import sys
import string
import random

def capitalized_string(length):
    return random.choice(string.letters[26:]) + ''.join(random.choice(string.letters[:26]) for _ in xrange(length - 1))
    
def iri_for(entity, ontology_iri):
    return '<{0}{1}{2}>'.format(ontology_iri, '#', entity)

def main(num_axioms, ontology_iri):
    pad = num_axioms / 10

    common_name = str(num_axioms).rjust(8, '0')
    file_a = open(common_name + 'a.owl', 'w')
    file_b = open(common_name + 'b.owl', 'w')
    def w(s):
        file_a.write(s)
        file_b.write(s)
    prefix_line = 'Prefix(:=<{0}{1}>)\n'.format(ontology_iri, '#')
    w(prefix_line)
    ontology_line = 'Ontology(<{0}>\n'.format(ontology_iri)
    w(ontology_line)

    # different axioms
    for _ in xrange(pad):
        class_name = ':' + capitalized_string(10)
        individual_name = ':' + capitalized_string(10)
        file_a.write('ClassAssertion({0} {1})\n'.format(class_name, individual_name))
        class_name = ':' + capitalized_string(10)
        individual_name = ':' + capitalized_string(10)
        file_b.write('ClassAssertion({0} {1})\n'.format(class_name, individual_name))
        
    # common axioms
    for _ in xrange(num_axioms - pad):
        class_name = ':' + capitalized_string(10)
        individual_name = ':' + capitalized_string(10)
        w('ClassAssertion({0} {1})\n'.format(class_name, individual_name))

        
    # close the ontology statement
    w(')\n')


if __name__ == '__main__':
    num_axioms = int(sys.argv[1])
    if len(sys.argv) > 2:
        ontology_iri = sys.argv[2]
    else:
        ontology_iri = 'http://ontology/test.owl'
    main(num_axioms, ontology_iri)