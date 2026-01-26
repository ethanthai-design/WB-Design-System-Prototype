import type { Meta, StoryObj } from '@storybook/angular';
import { ButtonComponent } from './button.component';

const meta: Meta<ButtonComponent> = {
    title: 'Components/Button',
    component: ButtonComponent,
    tags: ['autodocs'],
    argTypes: {
        variant: {
            control: 'select',
            options: ['primary', 'secondary-color', 'secondary-gray', 'tertiary-color', 'tertiary-gray', 'danger'],
        },
        size: {
            control: 'select',
            options: ['xs', 'sm', 'md', 'lg'],
        },
        icon: {
            control: 'text',
        },
    },
};

export default meta;
type Story = StoryObj<ButtonComponent>;

export const Primary: Story = {
    args: {
        label: 'Primary Button',
        variant: 'primary',
        size: 'md',
    },
};

export const SecondaryColor: Story = {
    name: 'Secondary Color',
    args: {
        label: 'Secondary Color',
        variant: 'secondary-color',
        size: 'md',
    },
};

export const SecondaryGray: Story = {
    name: 'Secondary Gray',
    args: {
        label: 'Secondary Gray',
        variant: 'secondary-gray',
        size: 'md',
    },
};

export const TertiaryColor: Story = {
    name: 'Tertiary Color',
    args: {
        label: 'Tertiary Color',
        variant: 'tertiary-color',
        size: 'md',
    },
};

export const TertiaryGray: Story = {
    name: 'Tertiary Gray',
    args: {
        label: 'Tertiary Gray',
        variant: 'tertiary-gray',
        size: 'md',
    },
};

export const Danger: Story = {
    args: {
        label: 'Danger Button',
        variant: 'danger',
        size: 'md',
    },
};

export const Sizes: Story = {
    render: (args) => ({
        props: args,
        template: `
      <div style="display: flex; flex-direction: column; gap: 16px; align-items: flex-start;">
        <wb-button label="Size LG" size="lg" variant="primary"></wb-button>
        <wb-button label="Size MD" size="md" variant="primary"></wb-button>
        <wb-button label="Size SM" size="sm" variant="primary"></wb-button>
        <wb-button label="Size XS" size="xs" variant="primary"></wb-button>
      </div>
    `,
    }),
};

export const WithIcon: Story = {
    args: {
        label: 'Button with Icon',
        icon: 'pi pi-check',
        variant: 'secondary-gray'
    },
};

export const Loading: Story = {
    args: {
        label: 'Submitting...',
        loading: true,
        variant: 'primary'
    },
};

export const Disabled: Story = {
    args: {
        label: 'Disabled Button',
        disabled: true,
        variant: 'primary'
    },
};
